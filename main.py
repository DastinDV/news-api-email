import requests
from send_email import send_email

topic = "tesla"

api = "9e88c356fcd74aa6a3f9262ef6d31c58"
url = f"https://newsapi.org/v2/everything?q={topic}" \
      "&from=2022-11-25&sortBy=publishedAt&apiKey=" \
      "9e88c356fcd74aa6a3f9262ef6d31c58"\
      "&language=ru"

request = requests.get(url)
content = request.json()

message = ""

for article in content["articles"][:10]:
    if article["title"] is not None:
        message += f"""\
Subject: Today's news
Title: {article["title"]}
Description: {article["description"]}
{article["url"]}
""" + "\n"

message = message.encode("utf-8")
send_email(message)
