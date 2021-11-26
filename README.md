# CS425 - Natural Language Communication
EzFinbot - A bot to provide financial advise easily<br>
(Disclaimer: We are not financial advisors, advise provided is from data from our dataset.)

## Dataset
FiQA-2018 dataset (https://sites.google.com/view/fiqa/home)

## Pre-requisites
- Python 3.6+
- Anaconda

## Set-up dependencies
- Run ```pip install -r requirements.txt``` in root directory

## How to run
1) Folders are split up into modules, where each module serves a function in the project process in sequence.
2) Intermediary files are outputted when running the code in each module.
3) Intermediary files are already included in this repo. However, if you wish to run the code to output intermediary files, just run the code in each folder <b>in sequence of numbers</b>
4) <b>Description of what each module does can be found in README inside each Folder</b>
5) To run telegram bot, simply open telegram and search for @EzFinBot to start using.<br>4.1. Telegram bot is already deployed with AWS Lightsail.<br>4.2. In the event we take down the bot, you may deploy/ run the telegram code locally<br>4.3. Telegram bot code can be found in <b>9.Deployment</b><br>4.4. (If bot is taken down) Simply run ```python ezfinbot-telegram.py``` in terminal and you can use the bot at @EzFinBot.<br>4.5. We will update this README if bot is taken down.
6) Alternatively, you may run chatbot locally.<br>5.1. Head to <b>9.Deployment</b><br>5.2. Run ```ezfinbot-cli.py```

## Project Description
This project's ultimate aim is to create a Information Retrieval based Question Answering platform to answer common financial questions. From a high-level perspective, the project flow involves:
1) Query expansion using SpaCy wordnet financial domain to expand nouns of user query
2) Retrieval with BERT models<br> 
2.1. Evaluated a few BERT models from sentence-transformers library. <br>2.2. Finetuned with SimCSE technique and evaluated MSMARCO-distilBERT and MSMARCO-BERTbase (both untuned and fine-tuned versions) and using cosine similarity to retrieve top 20 relevant documents to question.<br>2.3. Best performing BERT model (fine-tuned MSMARCO-BERTbase) was used as retrieval model<br>2.4. Results are evaluated using P@1, R@1, F1@1, and also qualitatively.
3) Reranker with cross encoder. Utilized ms-marco-miniLM-L-12-v2 as cross-encoder.<br>
3.1. This reranks the top 20 relevant documents retrieved by retrieval model.<br>3.2. Cross-encoders are more accurate but takes longer to run. Hence, we do not implement this on entire dataset. <br>3.3. Evaluation method similiar as using retrieval.
4) Deployment <br>4.1. Inside folder 9.Deployment, users can find code for telegram bot (ezfinbot-telegram.py), and code to run locally (ezfinbot-cli.py).<br>4.1. Telegram bot can be accessed at @EzFinBot.<br>4.2. Telegram bot is currently already hosted on AWS, so no need to run ezfinbot-telegram.py to use bot.




