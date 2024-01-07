import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_absolute(url):
    return bool(urlparse(url).netloc)

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    return [link['href'] for link in links]

def web_crawler(start_url, max_depth=3):
    visited_urls = set()

    def crawl(url, depth):
        if depth > max_depth or url in visited_urls:
            return

        print(f"Crawling: {url}")
        visited_urls.add(url)

        links = get_links(url)
        for link in links:
            absolute_url = urljoin(url, link)
            if is_absolute(absolute_url):
                crawl(absolute_url, depth + 1)

    crawl(start_url, depth=1)

if __name__ == "__main__":
    # Replace 'https://example.com' with the starting URL you want to crawl
    start_url = 'https://example.com'
    web_crawler(start_url, max_depth=3)
