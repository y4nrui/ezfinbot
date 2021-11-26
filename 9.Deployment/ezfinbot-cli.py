print()
print("EzFinBot> Getting my kopi, wait ah~~~")
import numpy as np
import pandas as pd
qna_df = pd.read_csv("../0.Datasets/QnA.csv")

import pickle
sentence_embeddings = pickle.load(open("../4.Retrieval/finetuned_bertbase/answer_embeddings.pkl",'rb'))

from sentence_transformers import SentenceTransformer
bi_encoder_model = SentenceTransformer("../10.Fine-tuned Models/finetuned-bertbase-1epoch")
from sentence_transformers.cross_encoder import CrossEncoder
cross_encoder_model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-12-v2')
print()
print("EzFinBot> Ok I've lim-ed my kopi~~~")
print()

def predict(user_message):
    # bi encoder - retriever
    question_embedding = bi_encoder_model.encode(user_message)
    answer_similiarity = {}
    for i,embed in enumerate(sentence_embeddings):
        answer_similiarity[i]= np.dot(question_embedding, embed)
    answer_similiarity = {k: v for k, v in sorted(answer_similiarity.items(), key=lambda item: item[1], reverse=True)}
    top_20_hits = []
    for item in list(answer_similiarity)[:20]:
        top_20_hits.append(qna_df['answer'].to_list()[item])
    
    # cross encoder - reranker
    cross_encoder_answer_similarity = {}
    for hit in top_20_hits:
        cross_encoder_answer_similarity[hit] = cross_encoder_model.predict([user_message,hit])
    cross_encoder_answer_similarity = {k: v for k, v in sorted(cross_encoder_answer_similarity.items(), key=lambda item: item[1], reverse=True)}
    # print(cross_encoder_answer_similarity)
    answer = list(cross_encoder_answer_similarity.keys())[0]
    return answer

while True:
    print("EzFinBot> If you anytime need to zao, just type 'end'!")
    print()
    user_message = input("EzFinBot> How can I help you? \n\nUser> ")
    if user_message == "end":
        print()
        print("EzFinBot> uWu~~~Sayonara~~~")
        print()
        break
    answer = predict(user_message)
    print()
    print("EzFinBot>", answer)
    print()