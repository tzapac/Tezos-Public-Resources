import requests
import json
import time
import pandas as pd
from google.oauth2 import service_account
import pandas_gbq

address = '<insert smart contract address>'
url = "https://api.tzstats.com/explorer/contract/"+address+"/calls?meta=1"

credentials = service_account.Credentials.from_service_account_file(
    '<insert json cred>',
)

pandas_gbq.context.credentials = credentials

pandas_gbq.context.project = "<insert project name>"

#create a function to test the status code. find the status code meaning in this link https://tzstats.com/docs/api#status-codes
def api_call_test():
    r = requests.get(url)
    code = r.status_code
    return code

#change response into a json format
def collect_api_response():
    r = requests.get(url)
    data = r.json()
    return data
        
#reformatting json data to a table friendly view
def clean_data(json_data): #reformats and unnest data to a wide format
    df = pd.json_normalize(json_data)
    df.columns = df.columns.str.replace(".", "_")
    df['time'] =  pd.to_datetime(df['time']) #reformatting to date time for time series graphs
    return df

#uploading to bigquery
def bq_upload(dataframe):
    dataframe.to_gbq('smartcon_test.example',if_exists='replace') #set to replace to refresh new data. when data gets too big, better to append instead

#tie the code together
def full_code():
    test = api_call_test()
    
    if test == 200:
        jsondata = collect_api_response()
    
    else:
        time.sleep(10)
        test = api_call_test()
        if test == 200:
            jsondata = collect_api_response()
            
        else:
            assert 5+5=11 #forces script to throw an error and stop
    
    clean_df = clean_data(jsondata)
    bq_upload(clean_df)

if __name__ == '__main__':
    full_code()