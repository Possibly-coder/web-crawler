import json
from crawler.extractors import tatacliq, virgio, nykaafashion, westside


def run_all_extractors():
    urls = {}
    urls["https://www.virgio.com"] = virgio.extract()
    urls["https://www.tatacliq.com"] = tatacliq.extract()
    urls["https://www.nykaafashion.com"] = nykaafashion.extract()
    urls["https://www.westside.com"] = westside.extract()

    with open("output/product_urls.json", "w") as f:
        json.dump(urls, f, indent=4)