# Objective
To learn how to connect OpenAI, Pincone and Streamlit in order to create a custom search engine tool.

## Logic

This repository:

- Reads `sitemap` from the domain in xml format
- Converts the xml to json and exports the urls to url `folder`
- Scrapes the page title, header and body and saves to `pages` 
- Builds a training dataset by combining all scraped pages into `data.csv`
- Creates embeddings the combination of `header` and `title` using `text-embedding-ada-002`
- Stores embeddings to `pinecone` database
- Build `streamlit app` to query embeddings with custom questions

## Known issues

- Only 25% of urls have been scraped due to timings and PoC state of project
- The `body` of information collected requires large amounts of preprocessing. Perhaps requiring a preprocess module or further improvement to web-scraper
- In doing so, the embeddings can be created on the full text of `body` and then displaying the full information

## Useful Documents

- https://github.com/pinecone-io/examples/blob/master/integrations/openai/semantic_search_openai.ipynb