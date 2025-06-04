import requests

query=input("What type of news you interestedin today? ")

api="8e9b20b583654e6caae1207340ad6f4f"

url= f"https://newsapi.org/v2/everything?q={query}&from=2025-05-04&sortBy=popularity&apiKey={api}"
# url= f"https://newsapi.org/v2/everything?q={query}&from=2025-06-02&apiKey={api}"

print(url)

r= requests.get(url)
data= r.json()
articles = data["articles"]

for article in articles:
    print(article["title"], article["url"])
    print("\n***************************\n")