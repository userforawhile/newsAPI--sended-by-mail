import requests

ap_key = "efb3227ce9554da58e04d5ed8f3b6c03"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=efb3227ce9554da58e04d5ed8f3b6c03"

# made a request
request = requests.get(url)
# get a dictionary with data
content = request.json()

# access the article files and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])