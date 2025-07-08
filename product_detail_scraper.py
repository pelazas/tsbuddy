from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from typing import Optional

def scrape_product_details(url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.goto(url, timeout=60000)

        # Wait for page to load
        page.wait_for_timeout(3000)

        rating_text = None
        summary_text = None

        try:
            rating_elem = page.query_selector('span[data-hook="rating-out-of-text"]')
            rating_text = rating_elem.inner_text().strip() if rating_elem else None
        except:
            pass

        try:
            histogram_text = page.locator("#histogramTable").inner_text()

                        
        except Exception as e:
            print(f"Error extracting summary: {e}")
            pass

        browser.close()

        return {
            "rating": rating_text,
            "rating_distribution": histogram_text,
        }