import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_headlines(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This selector changes based on the website (e.g., 'h3' for BBC)
    headlines = [h.text.strip() for h in soup.find_all('h3')[:10]]
    
    filename = f"news_{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(filename, 'w') as f:
        f.write(f"Top Headlines for {datetime.now()}\n")
        f.write("="*30 + "\n")
        for i, line in enumerate(headlines, 1):
            f.write(f"{i}. {line}\n")
            
    print(f"Saved {len(headlines)} headlines to {filename}")

# scrape_headlines("https://www.bbc.com/news")