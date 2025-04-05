from crawler.utils import get_internal_links, is_product_url, fetch_page

def extract():
    base_url = "https://www.westside.com"
    to_visit = {base_url}
    visited = set()
    product_urls = set()

    while to_visit:
        url = to_visit.pop()
        visited.add(url)
        html = fetch_page(url)
        if not html:
            continue
        links = get_internal_links(base_url, html)
        for link in links:
            if link not in visited:
                to_visit.add(link)
            if is_product_url(link):
                product_urls.add(link)

    return list(product_urls)