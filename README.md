# TF-IDF & Cosine Similarity

內容:

1.TF-IDF.py: 主要腳本

  說明: 新聞載入 -> 繁體字典載入 -> 停用字典載入 -> TF-IDF計算 -> Cosine Similarity（相似文本比較）

2.dict.txt-v2.big: 擴充繁體字典

  說明: 此字典是基於官方繁體字典下，另外添加mlb相關關鍵字的字典，幫助Jieba切出正確的詞．

3.stopwords.txt: 停用字典

  說明:過濾掉不參與TF-IDF計算的字典

4.news.json: 新聞文本

  說明:新聞Json格式


用途：

1.TF-IDF:可計算出每篇文章的關鍵字

2.Cosine Similarity: 透過斷詞後的文本，可計算文本與本文之間的相似度，亦可用來比較句子跟句子之間的相似度
