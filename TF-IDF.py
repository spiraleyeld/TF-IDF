# coding:utf-8  
###  ====================== 後端測試區 - TF-IDF =========================
import json, jieba, re, os, sys, time
from datetime import datetime
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfVectorizer

### 載入要parse的資料
allData = []
for dataName in range(1,2):    
    with open('news.json'.format(dataName), 'r',encoding='utf-8') as f:
        data = json.load(f)
        print('Deal with data{}.json'.format(dataName))
        allData += data
### 載入繁體擴充字典
jieba.set_dictionary('dict.txt-v2.big')    

### 載入停用字
print('Input Stop Words')
stopwordset = set()
with open('stopwords.txt','r',encoding='utf-8') as sw:
    for line in sw:
        stopwordset.add(line.strip('\n'))

print('Start Jieba Cut')
totalContent = []
### 從data中挑1000篇文章切詞 - 特別注意，這行的迴圈數字決定參予tf-idf計算的文章數量
for i in range(0,50):
    article = ''
    content = allData[i]['Content']
    
    ### 斷詞, 產生一個結巴物件
    words = jieba.cut(content, cut_all=False)
    for word in words:   
        ### 正規表達式，只針對文字處理
        m = re.match(r'^[\u4E00-\u9FFFa-zA-Z]+$',word )
        if m is not None:
            if word not in stopwordset:
                article+=word
                article+=' '
    totalContent.append(article)

## 用來裝全部文章的權重值
textWeightList = []

## 用來裝前5權重值
tagList = []

### TF-IDF 開始計算
print('Start Tf-Idf')
if __name__ == "__main__":  
   
    tfIdfVectorizer = TfidfVectorizer()    
    tfIdf = tfIdfVectorizer.fit_transform(totalContent)    
    ## 取得詞袋模型中的所有詞語 
    myWord=tfIdfVectorizer.get_feature_names()        
    ## 將tf-idf矩陣抽取出來， j詞在第i篇文章中的tf-idf權重 
    weight=tfIdf.toarray()        
    for i in range(len(weight)):
        ## 用來裝單篇權重值
        textMining = {}       
        for j in range(len(myWord)):             
            ##print( myWord[j],weight[i][j] ) 
            textMining[myWord[j]] = weight[i][j]
        textWeightList.append(textMining)


print('Sorted the Weight of KeyWords')
### 權重排序 lanbda式
for oneArticle in textWeightList:
    dict= sorted(oneArticle.items(), key=lambda d:d[1], reverse = True)

    ### 決定要放幾個tag
    tag = []
    for i in range(0,5):
        tag.append(dict[i][0])
    tagList.append(tag)
        
### 將關鍵詞放進與其所對應的新聞
for i in range(len(tagList)):
    allData[i]['Tag'] =tagList[i]
