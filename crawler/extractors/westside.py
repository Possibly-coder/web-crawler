from crawler.utils import get_internal_links, is_product_url, fetch_page
import json, os
def extract():
    base_url = "https://www.westside.com"
    to_visit = {base_url}
    visited = set()
    product_urls = set()

    # Load already stored URLs (if resuming)
    output_path = "output/product_urls.json"
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
                product_urls.add(link)
                print("this is a product url: ", link)
                # Immediately write to file
                with open(output_path, "w") as f:
                    json.dump(sorted(product_urls), f, indent=4)
    return list(product_urls)