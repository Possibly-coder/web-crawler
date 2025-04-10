import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

# DOMAIN_PATTERNS = {
#     "virgio.com": ["/shop/"],
#     "tatacliq.com": ["/p/", "/product/"],
#     "nykaafashion.com": ["/p/"],
#     "westside.com": ["/product/", "/products/"],
# }

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
    path = urlparse(url).path.lower()

    # These are general patterns found across most e-com sites
    dynamic_patterns = [
        "/product", "/item", "/p", "/shop", "/products",
        "/store", "/buy", "/detail", "/prod", "/catalog"
    ]

    return any(pattern in path for pattern in dynamic_patterns)


    # domain_patterns = DOMAIN_PATTERNS.get(domain.replace('www.', ''), default_patterns)
    # patterns = [r"/product/", r"/p/", r"/item/"]
    # return any(re.search(pattern,url) for pattern in patterns)

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error Fetching {url}, {e}")
    return ""

