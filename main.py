import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime
import os
import requests
import json

load_dotenv()

news_api_key = os.environ.get("NEWS_API_KEY")

client = openai.OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
model = "gpt-4"

def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everythong?q={topic}&apiKey={news_api_key}&pageSize=5"
    )

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)

            data = news_json

            ##  Access all fields, loop through ==
            status = data["status"]
            total_results = data["totalReults"]
            articles = data["articles"]

            ## Loop through articles
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]




    except requests.exceptions.RequestException as e:
        print("Error occurred durinng API Request", e)

def main():
    pass


if __name__ == "__main__":
    main()
