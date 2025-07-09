# TechShoppingBuddy

This project is an AI-powered assistant that helps users make smarter purchase decisions in the consumer electronics space. It automates product search, spec comparison, review analysis, and ranks products based on price-to-value ratio.

## How it Works

The project follows a pipeline structure, where each step is handled by a specific agent:

1.  **User Input (`agents/user_input_agent.py`):** Processes the user's natural language query to extract the essential information for a product search.

2.  **Product Scraping (`scrapers/scrape_products.py`):** Takes the parsed user query and searches for products on Amazon, scraping the search results to get a list of products, including their titles, prices, and URLs.

3.  **Evaluation (`agents/evaluation_agent.py`):** Takes the scraped product information and uses a large language model (LLM) to analyze it, assigning a quality score from 1 to 10 based on the product's price, specifications, and ratings.

4.  **Formatting (`agents/formatting_agent.py`):** Takes the evaluated products and formats them into a clear and readable format, adding a title and a summary of the results.

5.  **Execution (`main.py`):** The `main.py` script orchestrates the entire pipeline. It calls the user input agent, the scraping agent, the evaluation agent, and the formatting agent in sequence. Finally, it prints the formatted results.

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
│   ├───user_input_agent.py
│   └───formatting_agent.py
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
*   `agents/formatting_agent.py`: Formats the evaluated products into a clear and readable format.
*   `requirements.txt`: Lists the Python dependencies for the project.
*   `README.md`: Provides a high-level overview of the project.

## How to Run

1.  Install the dependencies: `pip install -r requirements.txt`
2.  Create a `.env` file in the root directory and add your Anthropic API key:
    ```
    ANTHROPIC_API_KEY=your_api_key
    ```
3.  Run the main script: `python main.py`
4.  Enter a description of the product you are looking for when prompted.