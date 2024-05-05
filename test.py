import requests
from bs4 import BeautifulSoup
import main

def extract_article(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract article title
        title = soup.find('h1', class_=['entry-title','tdb-title-text']).text.strip()
        
        # Extract article content
        article_content = soup.find('div', class_='td-post-content tagdiv-type')
        if article_content:
            paragraphs = article_content.find_all('p')
            content = '\n'.join([p.text.strip() for p in paragraphs])
            return title, content
        else:
            print("No article content found on the page:", url)
            return None, None
    else:
        print("Failed to retrieve the webpage:", url)
        return None, None

import os

j = 0
for id in main.url_id:
    url = f'{main.urls[j]}'
    title, content = extract_article(url)
    if title and content:
        with open(f'Files/{id}.txt', 'w', encoding='utf-8') as file:
            file.write('{}\n{}'.format(title, content))
    j += 1
