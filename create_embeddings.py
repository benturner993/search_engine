import pandas as pd
import openai
import os
import pinecone
import keys

from tqdm.auto import tqdm

# static variables
index_name = 'semantic-search-openai'
pinecone_env='gcp-starter'
MODEL = "text-embedding-ada-002"
openai.api_key = keys.OPENAI_API_KEY

# read data
df=pd.read_csv('data/data.csv')
print('dataset read...')

# initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(
    api_key=keys.PINECONE_API_KEY,
    environment=pinecone_env  # find next to api key in console
)
print('pinecone initiated...')

# code to delete vectordb (remove existing)
if index_name in pinecone.list_indexes():
    pinecone.delete_index(index_name)

# check if 'openai' index already exists (only create index if not)
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536)

# connect to index
index = pinecone.Index(index_name)
print('connected to pinecone...')

count = 0  # we'll use the count to create unique IDs
batch_size = 32  # process everything in batches of 32
for i in tqdm(range(0, len(list(df['text'])), batch_size)):
    
    # set end position of batch
    i_end = min(i+batch_size, len(list(df['text'])))

    # get batch of lines and IDs
    lines_batch = list(df['text'])[i: i+batch_size]
    ids_batch = [str(n) for n in range(i, i_end)]
    
    # create embeddings
    res = openai.Embedding.create(input=lines_batch, engine=MODEL)
    embeds = [record['embedding'] for record in res['data']]
    
    # prep metadata and upsert batch
    meta = [{'text': line} for line in lines_batch]
    to_upsert = zip(ids_batch, embeds, meta)
    
    # upsert to Pinecone
    index.upsert(vectors=list(to_upsert))
print('embeddings created...')