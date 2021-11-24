# importing libraries
import requests
import json
import os
import pickle
import pandas as pd

#!pip install aiohttp
import aiohttp
import asyncio
import time

# setting REST API parameters
clientId = "sb-5ef56e02-73a0-425d-add6-ae76de56d7a6-CLONE-BS-RT!b40741|cai-production!b20881"
secret = "binding-5ef56e02-73a0-425d-add6-ae76de56d7a6$L_YFqjgLUUPH9BQObHVnnNCmzyZFKiXSHDAv6TZhVuM="
requestToken = "f7df95de81789c3221d8bac32696a920"
oauthURL = "https://sapcai-community.authentication.eu10.hana.ondemand.com/oauth/token"
requestURL = "https://api.cai.tools.sap/build/v1/dialog"

# get sap eval dataset
sap_df = pd.read_csv("../0.Datasets/train_test_split/test.csv", encoding='utf-8')
sample_qns = sap_df['question'].tolist()[:10]

def get_token():
    result = requests.post(oauthURL, data={'grant_type': 'client_credentials'}, auth=(clientId, secret))
    token = json.loads(result.content)
    return token["access_token"]

start_time = time.time()
async def main():
    # get all responses
    async with aiohttp.ClientSession() as session:
        predictions = []
        for qn in sample_qns:
            payload = json.dumps({
                "message": {
                    "content": qn,
                    "type": "text"
                },
                "conversation_id": "anything_goes_here_11111"
            })
            prediction = asyncio.ensure_future(
                get_async_response(session, payload))
            predictions.append(prediction)

        all_predictions = await asyncio.gather(*predictions)

    print('Number of predictions:', len(all_predictions))
    print(all_predictions)
    
# get single response
async def get_async_response(session, payload):

    async with session.post(requestURL, data=payload,
                            headers={"Authorization": "Bearer " +
                                     bearer, "X-Token": "Token " + requestToken,
                                     "Content-Type": "application/json"}
                            ) as response:
        result_data = await response.json()
        message = result_data['results']['messages'][0]['content']
        return message

bearer = get_token()
asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))
