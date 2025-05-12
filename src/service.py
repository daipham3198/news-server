import json
import ai

with open("pages.json", "r") as file:
    pages = json.load(file)

def get_pages():
    return pages

def get_news(page_name):
    page = pages[page_name]

    return ai.get_news(page["url"], page["tag"])