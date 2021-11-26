## Description
1) This folder contains one notebook, as part of our reranking step, used as part of our retrieve and rerank pipeline
2) The code calls on our best performing retrieval model, and implement reranking with cross-encoders on top of it.
3) In this case, our best performing retrieval model is from <b>10.Fine-tuned Models/finetuned_bertbase-1epoch</b>
4) If you would like to change the retrieval model, please change the above filepath to the location of your preferred model.
5) This notebook saves prediction to <b>7.Evaluate</b>
