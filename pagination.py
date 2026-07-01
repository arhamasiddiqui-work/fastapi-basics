# Pagination: large data ko page mai divide krke bhejna

from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests  # httpRequest send krne ke liye

app = FastAPI()


@app.get("/news")
def get_news(page: int = 1, limit: int = 5):
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = []

    for item in soup.find_all(
        "p", class_="Dundee-styles__DescriptionStyled-sc-50abbc98-0 eUixcX"
    ):
        title.append(item.text)

        # Pagination logic
        start = (page - 1) * limit
        end = start + limit

        return {
            "page": page,  #  current page
            "limit": limit,  #   items per page
            "total": len(title),
            "data": title,
        }
