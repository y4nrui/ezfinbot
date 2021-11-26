## Description
1) This folder contains .pkl files of predictions from all previous folders, and a metric_calculation.ipynb notebook
2) metric_calculation.ipynb <b>checks for and evaluates predictions from all files that are not metric_calculation.ipynb and .ipynb_checkpoints files</b>
3) Hence, please <b>ensure that only .pkl files of predictions, and metric_calculation.ipynb</b> are present in directory
4) Code in notebook prints out score for Precision@1, Recall@1, F1@1 for each prediction.
5) Take note in naming convention:<br>5.1. bm25_baseline refers to results for using BM25 as prediction method<br>5.2. cross_encoder refers to predictions for using finetuned-bertbase as retrieval and cross-encoder for reranking<br>
5.3. finetuned_bertbase_results refers to predictions using fine tuned bertbase only (using cosine similarity -> explained in report)<br>
5.4. finetuned_distilbert_results refers to predictions using fine tuned distilbert only<br>
5.5. query_expansion refers to perdictions using first implementation of query expansion (NLTK expansion of nouns with synonyms), along with entire retrieve and rerank pipeline<br>
5.6. updated_query_expansion refers to perdictions using second implementation of query expansion (SpaCy expansion of nouns with financial synonyms), along with entire retrieve and rerank pipeline<br>
5.7. untuned_distilbert_results refers to predictions using untuned distilbert only<br>
5.8. untuned_bertbase_results refers to predictions using untuned bertbase only
<br><br>
![image](https://user-images.githubusercontent.com/31071751/143568515-e4c4b228-37d2-4e72-89f8-93df60d8ee2b.png)
