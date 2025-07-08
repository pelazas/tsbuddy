# TechShoppingBuddy

This project is an AI-powered assistant that helps users make smarter purchase decisions in the consumer electronics space. It automates product search, spec comparison, review analysis, and ranks products based on price-to-value ratio.

## How it Works

The project follows a pipeline structure, where each step is handled by a specific module:

1.  **User Input (`main.py`, `agents/user_input_agent.py`):** The `main.py` script starts the pipeline by getting user input. The `user_input_agent.py` then processes this natural language query to extract the essential information for a product search.

2.  **Product Scraping (`scrapers/scrape_products.py`, `scrapers/product_detail_scraper.py`):**
    *   `scrape_products.py`: Takes the parsed user query and searches for products on Amazon. It scrapes the search results to get a list of products, including their titles, prices, and URLs.
    *   `product_detail_scraper.py`: For each product found, this script visits the product's page and scrapes detailed information, such as specifications, ratings, and rating distributions.

3.  **Evaluation (`agents/evaluation_agent.py`):** The `evaluation_agent.py` takes the scraped product information and uses a large language model (LLM) to analyze it. It assigns a quality score from 1 to 10 based on the product's price, specifications, and ratings.

4.  **Execution (`main.py`):** The `main.py` script orchestrates the entire pipeline. It calls the user input agent, the scraping agents, and the evaluation agent in sequence. Finally, it prints the evaluation result for the first product found.

## Project Structure

```
/Users/pelazas/Desktop/tsbuddy/
├───.gitignore
├───main.py
├───README.md
├───requirements.txt
├───agents/
│   ├───__init__.py
│   ├───evaluation_agent.py
│   └───user_input_agent.py
└───scrapers/
    ├───product_detail_scraper.py
    └───scrape_products.py
```

### Key Files

*   `main.py`: The entry point of the application. It orchestrates the entire pipeline from user input to product evaluation.
*   `agents/user_input_agent.py`: Parses the user's natural language query into a concise search query.
*   `scrapers/scrape_products.py`: Scrapes Amazon search results for a given query.
*   `scrapers/product_detail_scraper.py`: Scrapes the details of a single product page.
*   `agents/evaluation_agent.py`: Evaluates a product based on its scraped data and provides a score and explanation.
*   `requirements.txt`: Lists the Python dependencies for the project.
*   `README.md`: Provides a high-level overview of the project.

## How to Run

1.  Install the dependencies: `pip install -r requirements.txt`
2.  Run the main script: `python main.py`
3.  Enter a description of the product you are looking for when prompted.