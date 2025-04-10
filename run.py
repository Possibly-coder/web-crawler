import sys
from crawler.main import crawl_domain

if __name__ == "__main__":
    # below line takes care of the situation where if the user runs run.py with a url next to it, we would crawl only for that url
    domains = sys.argv[1:] or [
        "https://www.westside.com"
    ]

    for domain in domains:
        print(f"🔍 Crawling {domain}...")
        products = crawl_domain(domain)
        print(f"✅ Found {len(products)} products at {domain}")
