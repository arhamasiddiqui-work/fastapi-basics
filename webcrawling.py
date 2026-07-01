#  Web crawling: web ka data extract krna automatically, legal for few websites
#  BeautifulSoup: html ko parse krne ke liye

from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests     #httpRequest send krne ke liye

app=FastAPI()

@app.get("/news")
def get_news():
    url="https://www.bbc.com/news"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    title=[]
    for item in soup.find_all("div",class_="IndexCardHeading-styles__TitleWrapperStyled-sc-c7d910a6-0 hEhfIe"):
        title.append(item.text)
        return{
            "news":title
        }
