## Description
1) This folder contains a query_expansion_v2.ipynb file, which contains <b>two implementations of query expansion</b>
2) The first implementation utilizes NLTK wordnet to expand nouns in user query by using synonyms of the nouns
3) The second implementation utilizes SpaCy wordnet to expand nouns in usr query by using <b>financial synonyms</b> of the nouns
4) Both of these query expansion implementations are implemented with the full process flow of retrieve models and rerank models
5) We utilize our fine tuned model as a retrieval step from <b>0.Fine-tuned Models/finetuned_bertbase-1epoch</b>
6) You may edit the filepath in the code to change the retrieval model, but careless changing may result in error
7) Output of predictions with query expansion, and retrieve and rerank is saved to <b>7.Evaluate</b>
