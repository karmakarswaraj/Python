from newsapi import NewsApiClient

# Create a NewsApiClient object with your API key
newsapi = NewsApiClient(api_key='0d5a98d2f18d47e8a05310d109e93188')

# Get the top headlines
top_headlines = newsapi.get_top_headlines()

# Print the headlines
for article in top_headlines['articles']:
    print(article['title'])
