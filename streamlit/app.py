import pandas as pd
import numpy as np
import streamlit as st
import openai
import pinecone

# static variables
MODEL = "text-embedding-ada-002"
index_name = 'semantic-search-openai'
pinecone_env='gcp-starter'

# keys
openai.key = st.secrets["OPENAI_API_KEY"]
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]


@st.cache_data
def load_data():
    df = pd.read_csv('data/data.csv')
    return df

def main():

    st.image("streamlit/img/bupa_logo.png", width=60)
    st.image("streamlit/img/background.png")

    # load underlying data
    df=load_data()

    # initialize connection to pinecone (get API key at app.pinecone.io)
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=pinecone_env  # find next to api key in console
    )
    
    # connect to pinecone index
    index = pinecone.Index(index_name)

    # search box
    search_term = st.text_input(
        label="",
        placeholder="Please search bupa.co.uk for..."
    )

    if search_term:
        xq = openai.Embedding.create(input=search_term, engine=MODEL)['data'][0]['embedding']
        res = index.query([xq], top_k=5, include_metadata=True)

        # Iterate through the results and display the similarity and notes
        for match in res['matches']:

            # filter dataframe by index
            filtered_df = df[df.index == int(match['id'])]

            # Write results
            st.subheader(filtered_df['title'].values[0])
            st.write('Similarity: ',match['score'])
            st.write(filtered_df['url'].values[0])   

    st.markdown('''Created by Ben Turner as a **proof-of-concept only**.''')
      
if __name__ == '__main__':
    main()