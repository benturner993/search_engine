# Objective

- To build a new search functionality for `bupa.co.uk`. 
- To learn how to combine `OpenAI`, `Pinecone` and `Streamlit`.

## High Level Description

This repository:

- Downloads the `sitemap` from the domain (`https://www.bupa.co.uk/sitemap.xml`) in xml format
- Converts the xml to json and exports the urls to `url` folder
- For each url, the `scrape_page.ipynb` utility scrapes the page title, header and body and saves to `pages` folder 
- For each scraped page, the `build_dataset.ipynb` utility builds a training dataset by combining all scraped pages into `data.csv`
- The `create_embeddings.py` creates the embeddings for each page using a combination of `header` and `title` using `text-embedding-ada-002`
- The embeddings are saved to `pinecone` database
- Using a streamlit app running from `app.py`, a user can query the embeddings with custom questions and searches

## Logic / Workflow Diagram

![web_search](/img/hld_workflow.png)

## Route-To-Value

This proof of concept proves that it is possible to create a new search engine using a combination of open-source and cloud services.  

To achieve value from this PoC, an internal equivalent can be built and consumed. Equally, and potentially an easier route-to-value would be to build a stand-alone API which can be directly consumed from the `bupa.co.uk` website. 

## Known Issues

- Only 25% of urls have been scraped due to timings and PoC state of project  
- The `body` of information collected requires large amounts of preprocessing. Perhaps requiring a preprocess module or further improvement to web-scraper  
- In doing so, the embeddings can be created on the full text of `body` and then displaying the full information  

## Useful Documents

- https://github.com/pinecone-io/examples/blob/master/integrations/openai/semantic_search_openai.ipynb