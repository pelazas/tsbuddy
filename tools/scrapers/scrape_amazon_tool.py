from playwright.sync_api import sync_playwright
from tools.scrapers.product_detail_scraper import scrape_product_details

from bs4 import BeautifulSoup
import urllib.parse


def amazon_search_url(query: str) -> str:
    base_url = "https://www.amazon.es/s"
    params = {"k": query}
    query_string = urllib.parse.urlencode(params)
    return f"{base_url}?{query_string}"

def run(query, numberOfProducts) -> list:
    url = amazon_search_url(query)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.goto(url)
        page.wait_for_selector("div.s-main-slot")

        results_container = page.query_selector("div.s-main-slot")
        html_content = results_container.inner_html() if results_container else ""

        browser.close()

    soup = BeautifulSoup(html_content, "html.parser")

    product_divs = soup.find_all("div", attrs={"role": "listitem"})

    search_results = []

    print(f"Found {len(product_divs)} products for query: {query}")
    print(f"Scraping the first {numberOfProducts} products...")
    i = 0

    for product in product_divs[:numberOfProducts]:
        title_elem = product.find("h2")
        link_elem = product.find("a", class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal")
        price_whole = product.find("span", class_="a-price-whole")
        price_frac = product.find("span", class_="a-price-fraction")
        price_symbol_elem = product.find("span", class_="a-price-symbol")
        price_symbol = price_symbol_elem.get_text(strip=True) if price_symbol_elem else ""

        title = title_elem.get_text(strip=True) if title_elem else None
        url = "https://www.amazon.es" + link_elem["href"] if link_elem else None
        price = f"{price_whole.text}{price_frac.text}{price_symbol}" if price_whole and price_frac else None

        details = scrape_product_details(url) if url else {}

        search_results.append({
            "title": title,
            "price": price,
            "url": url,
            "specs": details.get("specs"),
            "rating": details.get("rating"),
            "rating_distribution": details.get("rating_distribution", {}),
            "n_reviews": details.get("n_reviews"),
            "image_url": details.get("image_url")
        })
        i += 1
        print(f"* Scraped product {i}: {title}")
    
    return search_results

