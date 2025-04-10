# 🕷️ Web Crawler

A basic yet powerful Python web crawler to discover all **product URLs** from one or more e-commerce websites.

---

## 🚀 Features

- ✅ **URL Discovery** — Crawls all internal links on the website
- ✅ **Smart Product Detection** — Detects product pages using common patterns (e.g., `/product/`, `/item/`, etc.)
- ✅ **Supports Multiple Domains** — Crawl multiple websites in one go
- ✅ **Auto-Saves Results** — Saves found product URLs to `output/product_urls.json`
- ✅ **Customizable Patterns** — Easy to extend with more product path rules

---

## 🧠 How it Works

1. You provide the domain(s)
2. It crawls internal links recursively
3. It checks if a link is a product page based on URL structure
4. All matched product URLs are saved in a JSON file

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/Possible-coder/web-crawler.git
   cd web-crawler
2. **Install packages from requirements.txt**
    ```bash
    pip install -r requirements.txt