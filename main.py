import requests

api = "9e88c356fcd74aa6a3f9262ef6d31c58"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2022-11-25&sortBy=publishedAt&apiKey=" \
      "9e88c356fcd74aa6a3f9262ef6d31c58"

request = requests.get(url)
content = request.json() 

for article in content["articles"]:
      print(article["title"])
      print(article["description"])