from crawler.utils import get_internal_links, is_product_url, fetch_page
import json

def extract():

    base_url = "https://www.virgio.com"
    visited = set()
    to_visit = {base_url}
    product_urls = set()

    while to_visit:
        url = to_visit.pop()
        visited.add(url)
        html = fetch_page(url)
        if not html:
            continue
        links = get_internal_links(url, html)

        for link in links:
            if link not in visited:
                to_visit.add(link)
            if is_product_url(link):
                product_urls.add(link)
            with open("output/product_urls.json", "w") as f:
                json.dump(list(product_urls), f, indent=4)
    return list(product_urls)

