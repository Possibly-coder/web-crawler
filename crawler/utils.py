import re
from bs4 import BeautifulSoup
import requests

def get_internal_links(base_url, html):
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a in soup.find_all('a', href=True):
        href = a["href"]

        if href.startswith("/") or base_url in href:
            full_url = href if href.startswith("http") else base_url.rstrip("/") + href
            links.add(full_url)
    return links

def is_product_url(url):
    patterns = [r"/product/", r"/p/", r"/item/"]
    return any(re.search(pattern,url) for pattern in patterns)

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error Fetching {url}, {e}")
    return ""

