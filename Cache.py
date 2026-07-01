#  Caching in fastAPI: Saving data for a short time to make future requests faster
# TTL(time-to-live) config: How long cached data is kept before it is updated

from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import time

app = FastAPI()

# Cache storage
cache_data = []
last_fetch = 0


@app.get("/news")
def get_news():
    global cache_data, last_fetch   

    start = time.time()

    if time.time() - last_fetch > 60:
        print("Fetching fresh data...")

        url = "https://www.bbc.com/news"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        cache_data = [
            item.text.strip()
            for item in soup.find_all(
                "div",
                class_="IndexCardHeading-styles__TitleWrapperStyled-sc-c7d910a6-0 hEhfIe"
            )
        ]

        last_fetch = time.time()

    else:
        print("Fetching from cache...")

    end = time.time()
    time_taken = round(end - start, 5)

    return {
        "time_taken": time_taken,
        "news": cache_data
    }