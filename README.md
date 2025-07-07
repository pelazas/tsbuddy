# TechShoppingBuddy

**techshoppingbuddy.com** is an AI-powered assistant that helps users make smarter purchase decisions in the consumer electronics space. It automates product search, spec comparison, review analysis, and ranks products based on price-to-value ratio — so you don't waste time digging through dozens of tabs and biased reviews.

---

## 🚀 What It Does

- 🔍 Takes a natural language query (e.g., *“best noise cancelling headphones under 200€”*)
- 🌐 Searches product sources (Amazon, AliExpress, etc.) via API or scraping
- 📊 Normalizes product specifications and filters duplicates
- 💬 Analyzes customer reviews using LLMs
- 🧠 Ranks items using a customizable value score (specs × price × sentiment)
- 📝 Returns a report of top picks with reasoning, links, and scores

---

## 🧠 Why It Exists

Finding the *best* product online today means:
- Reading conflicting blog reviews
- Comparing specs across 20 tabs
- Evaluating fake ratings
- Making biased decisions from ads

This project builds an **autonomous shopping analyst** tool, streamlining the decision-making process using agents, scraping, and LLMs.

---

## 🧩 How It Works (Pipeline)

### 1. `user_input_agent.py`
Parses user query to extract:
- Product category
- Desired features
- Budget range
- Constraints (e.g. “battery life > 10h”)

### 2. `search_agent.py`
Scrapes or queries external APIs to find matching products.
Returns raw product data (titles, specs, price, URL, reviews).

### 3. `data_agent.py`
Cleans and structures data:
- Normalize units (e.g., GB, mAh)
- Remove duplicates
- Standardize fields across vendors

### 4. `review_agent.py`
Uses LLM (OpenAI, HF, etc.) to:
- Summarize reviews
- Detect common pros/cons
- Flag misleading patterns

### 5. `ranking_agent.py`
Applies a scoring function: ValueScore = (spec_weight × performance) + (sentiment_weight × review_score) - price_penalty
This agent ranks the best-value products per user criteria.

### 6. `report_agent.py`
Generates a final markdown or web-ready report:
- Top 3 picks
- Key specs
- Value scores
- Short AI-generated rationale
- Purchase links

