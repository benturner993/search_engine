# Objective
Create a search engine

# How does it work?

- Determine urls using web `sitemap`
- Scrape 25% of urls (for time)
- Create embeddings using `text-embedding-ada-002`
- Store embeddings in pinecone
- Build app to host model and query underlying data

# Useful Documents

- https://github.com/pinecone-io/examples/blob/master/integrations/openai/semantic_search_openai.ipynb