from crawler.utils import get_internal_links, is_product_url, fetch_page


def extract():
    base_url = "https://www.tatacliq.com"
    to_visit = {base_url}
    visited = set()
    product_urls = set()
    import ipdb; ipdb.set_trace()
    while to_visit:
        url=to_visit.pop()
        visited.add(url)
        html = fetch_page(url)
        if not html:
            continue
        links = get_internal_links(url, html)
        for link in links:
            if link not in visited:
                to_visit.add(link)
            if is_product_url(url):
                product_urls.add(url)
    return product_urls

