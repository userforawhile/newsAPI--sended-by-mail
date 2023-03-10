import requests
from send_email import send_email

topic = "tesla"

ap_key = "efb3227ce9554da58e04d5ed8f3b6c03"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=efb3227ce9554da58e04d5ed8f3b6c03&" \
      "language=en"

# made a request
request = requests.get(url)
# get a dictionary with data
content = request.json()

# access the article files and description
body = ""
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + str(article["description"]) \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)