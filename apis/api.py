import requests
from send_mail import send_mail

api_key = "9516d70a090042d48ceefedeb4af642e"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-08-11&sortBy=publishedAt&" \
      "apiKey=9516d70a090042d48ceefedeb4af642e"

req = requests.get(url)

content = req.json()

body = ""
for article in content["articles"]:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_mail(message=body)



