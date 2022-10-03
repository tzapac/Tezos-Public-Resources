# Smart Contract Analysis
Hello world! Excited to have you onboard and start exploring tools on Tezos.

In this tutorial, I will guide you through:

1. First Steps - Setting up your PC and Google BigQuery
2. Connecting to Google Data Studio

## 1. First Steps - Setting up your PC and Google BigQuery

There are things that you need to have installed in your local machine before we could utilise the script. To prevent this from becoming too long, I've attached links to articles below. It should help you prep the environment needed to get this going.

+ Download files from this repo [click here](https://www.toolsqa.com/git/difference-between-git-clone-and-git-fork/#:~:text=When%20you%20fork%20a%20repository,with%20the%20help%20of%20Git.)
+ Install Python [click here](https://medium.com/bb-tutorials-and-thoughts/how-to-install-and-getting-started-with-python-acf369e4cf80)
+ Download the required packages from your terminal or command prompt `pip install -r /path/to/requirements.txt`

Phew, that was a long one. now to setup your BigQuery.

Proceed [here](https://cloud.google.com/bigquery) to start!

### Click on `Try BigQuery free`

<img width="1490" alt="image" src="https://user-images.githubusercontent.com/78521141/193473231-b31fae7f-8c7d-45ed-ae04-991eccba8037.png">

Fill up your details and payment method (don't worry, they won't actually charge you until you've activated). Proceed with `START MY FREE TRIAL`. They will prompt you with surverys and tutorials, but you can skip it if you don't want to. 

Congrats! you are can now utilise BigQuery free trial! You can consider activating it, since the costs for storage are relatively low (it won't break your bank). There are other tools that you can utilise as well. But for simplicity, I'll only be going through GCP's BigQuery. 

____________________

Next, let's create a service account for us to utilise the BigQuery API. This will allow us to authenticate access from our local machine.


### Hover on `IAM & Admin` and click on `Service Accounts`.

![image](https://user-images.githubusercontent.com/78521141/193473715-07425150-8633-4929-a013-42cb87a0187d.png)


### Click `CREATE SERVICE ACCOUNT`

![image](https://user-images.githubusercontent.com/78521141/193473777-cba6847d-0dd9-4c8b-8c4e-6dff80a337a6.png)


### Give the account a name then click `CREATE AND CONTINUE`

![image](https://user-images.githubusercontent.com/78521141/193473859-12db6c9b-bbbe-40b2-843c-8ee912c89a70.png)


Grant Access right to your project. Ideally, you would want it limited to only read and write access. For testing purposes, let's just use the Owner role. Do note that it is strongly not recommended for Production Environment.

<img width="543" alt="image" src="https://user-images.githubusercontent.com/78521141/193473993-807234fd-32b9-4761-a463-809f3507cefb.png">


### Once you've clicked on `DONE`, you should see that the status of your service account is ticked like below.

<img width="598" alt="image" src="https://user-images.githubusercontent.com/78521141/193474077-77b746d3-e145-4bea-bf09-84800df0cf4c.png">


### Create a key and download the json file. Enter your service account by clicking on its name. Go to `KEYS` tab then click on `ADD KEY` and `CREATE new key`.

![image](https://user-images.githubusercontent.com/78521141/193474180-d841fe87-e41a-410e-8d08-d04f0963e8d7.png)


### Check `JSON` option then click `CREATE`.

<img width="654" alt="image" src="https://user-images.githubusercontent.com/78521141/193474219-239a55bb-f02c-4f91-8fcc-e63ef6ad33e1.png">


This will automatically download the json credentials to your Downloads Folder.

____________________

### Create a dataset to load data into! Click [here](https://console.cloud.google.com/bigquery) to go to your project! Click on the options next to your project then `Create dataset`.

![image](https://user-images.githubusercontent.com/78521141/193474561-85eeb77c-70f6-4669-b537-1b1fd650623a.png)


Name your dataset and set the location to store the data. I've selected Singapore because, well, I feel comforted that it's stored here locally. But also, having it near you means it will also reduce latency.

<img width="549" alt="image" src="https://user-images.githubusercontent.com/78521141/193474648-f61cc188-97ff-4d06-b3af-bd3cf884e6e6.png">


Take not of the `project id` and the `dataset id`, you will need it later.

____________________

Now now, let's put it all together into the script! Open `tzstats_to_bq.py` and plug in the credentials!

```python
address = 'your smart contract address here

credentials = service_account.Credentials.from_service_account_file(
    'your json file location here',
)

pandas_gbq.context.project = 'your project id'

dataframe.to_gbq('your dataset id and table name',if_exists='replace')
```
Note: for dataset id and table name should be in this format `smart_contract_test.table1`

____________________

Woot woot! We have now finished our setup. You can fire it up from your IDE or even your terminal to begine collecting data!


A summary of what the script does, it's using an API endpoint from [tzstats](https://tzstats.com/) then uploading it to Google BigQuery. This is a free tool that we could use to extract data. If you are keen to explore more endpoints, refer to their API documentation [here](https://tzstats.com/docs/api#tezos-api). You could edit the endpoint easily and extract other data out as well!



## 2. Connecting to Google Data Studio

Now that you have your data in place, we need it to connect to a tool that we can use to play around with it. For this tutorial, I'll be utilising Google Data Studio. It's a free tool that you can use to fetch data from Google platforms. Do note that if you require it to fetch from external sources, there would be a cost behind it. Let's start by heading to the [site](https://datastudio.google.com/)

### Click on `Blank Report`. Fill in all the details accordingly if it's your first time using it. Afterwards, you would be prompted to add data to the report.

### Click on `BigQuery`

![image](https://user-images.githubusercontent.com/78521141/193475413-d872da3b-6046-43bb-852e-5589567110f1.png)


### Select your smart contract table and click `Add`

<img width="1497" alt="image" src="https://user-images.githubusercontent.com/78521141/193475501-d01ab244-7d92-471c-89b2-08bceb3c46a6.png">


Boom, you're done and data is connected. We're ready to create sleek charts.

