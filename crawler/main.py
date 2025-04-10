# crawler/main.py

from crawler.utils import get_internal_links, is_product_url, fetch_page
import json
import os
from urllib.parse import urlparse

def crawl_domain(base_url: str, output_dir="output"):
    visited = set()
    to_visit = {base_url}
    product_urls = set()

    # Use domain as filename
    domain = urlparse(base_url).netloc.replace("www.", "")
    output_path = os.path.join(output_dir, f"{domain}_products.json")

    # Resume progress if already exists
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            try:
                product_urls = set(json.load(f))
            except json.JSONDecodeError:
                product_urls = set()

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue
        visited.add(url)

        html = fetch_page(url)
        if not html:
            continue

        links = get_internal_links(base_url, html)
        for link in links:
            if link not in visited:
                to_visit.add(link)

            if is_product_url(link) and link not in product_urls:
                print("PRoduct url: ", link)
                product_urls.add(link)
                with open(output_path, "w") as f:
                    json.dump(sorted(product_urls), f, indent=4)

    return list(product_urls)
