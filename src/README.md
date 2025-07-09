# TechShoppingBuddy

This project is an AI-powered assistant that helps users make smarter purchase decisions in the consumer electronics space. It automates product search, spec comparison, review analysis, and ranks products based on price-to-value ratio.

## How it Works

The project follows a pipeline structure, where each step is handled by a specific tool:

1.  **User Input:** The user is prompted to describe the product they are looking for.

2.  **Product Scraping (`tools/scrapers/scrape_amazon_tool.py`):** Takes the user's query and searches for products on Amazon, scraping the search results to get a list of products, including their titles, prices, and URLs.

3.  **Product Evaluation:** The scraped product information is then evaluated by a large language model (LLM) to assign a quality score from 1 to 10 based on the product's price, specifications, and ratings.

4.  **Data Formatting (`tools/formatting_tool.py`):** The evaluated products are formatted to be saved to a database.

5.  **Database Storage (`database.py`):** The formatted products are then saved to a MongoDB database.

6.  **Execution (`main.py`):** The `main.py` script orchestrates the entire pipeline. It calls the scraping tool, the evaluation logic, the formatting tool, and the database module in sequence. Finally, it prints the formatted results.

## Project Structure

```
/Users/pelazas/Desktop/tsbuddy/
├───.gitignore
├───main.py
├───README.md
├───requirements.txt
├───database.py
└───tools/
    ├───scrapers/
    │   ├───product_detail_scraper.py
    │   └───scrape_amazon_tool.py
    └───formatting_tool.py
```

### Key Files

*   `main.py`: The entry point of the application. It orchestrates the entire pipeline from user input to product evaluation.
*   `database.py`: Handles the connection to the MongoDB database and saves the products.
*   `tools/scrapers/scrape_amazon_tool.py`: Scrapes Amazon search results for a given query.
*   `tools/scrapers/product_detail_scraper.py`: Scrapes the details of a single product page.
*   `tools/formatting_tool.py`: Formats the evaluated products to be saved to a database.
*   `requirements.txt`: Lists the Python dependencies for the project.
*   `README.md`: Provides a high-level overview of the project.

## How to Run

1. Create a virtual environment, source into it.
1.  Install the dependencies: `pip install -r requirements.txt`
2.  Make sure you have a MongoDB instance running on `mongodb://localhost:27017/`.
3.  Create a `.env` file in the root directory and add your Anthropic API key:
    ```
    ANTHROPIC_API_KEY=your_api_key
    ```
4.  Run the main script: `python main.py`
5.  Enter a description of the product you are looking for when prompted.