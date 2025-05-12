from bs4 import BeautifulSoup
import requests
import json
import re

def get_page_listing_content(page, tag):
    response = requests.get(page)

    if response.status_code == 200:
        html = response.text
    else:
        print(f"Failed to retrieve HTML. Status code: {response.status_code}")

    soup = BeautifulSoup(html, 'html.parser')
    if(tag):
        content = soup.find('div', class_=tag)
    else:
        content = html
    
    return content

def content_to_json(raw_json):
    cleaned = re.sub(r"^```json|```$", "", raw_json.strip(), flags=re.MULTILINE).strip()
    data = json.loads(cleaned)
    return data
