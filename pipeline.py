from agents import user_input_agent
from agents.evaluation_agent import run as evaluation_run
from tools.formatting_tool import formatProducts
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from tools.scrapers import scrape_amazon_tool
from tools.database import save_products_to_db

class State(TypedDict):
    messages: Annotated[list, add_messages]
    products: list

def run_pipeline(query, category, numberOfProducts):
    input_category = category
    user_input = query

    # 1. Initialize state
    state: State = {
        "messages": [{"role": "user", "content": user_input}],
        "products": [],
    }

    # 2. User Input Agent with the user's query
    user_query_result = user_input_agent.run(state)
    state["messages"].extend(user_query_result["messages"])

    # 3. Call the run method in scrape_products.py with the parsed query, store the search_results in the state
    parsed_query = state["messages"][-1]["content"]
    search_results = scrape_amazon_tool.run(parsed_query, numberOfProducts)
    state["products"].extend(search_results)

    # 4. Call the Evaluation agent with the state, print the evaluation results
    print("\n"+40*'*')
    print("Evaluating Products...")
    if search_results and len(search_results) > 0:
        evaluation_result = evaluation_run(state)
        print("Evaluation Result:")
        print(evaluation_result["messages"][0]["content"])
    else:
        print("No products found.")

    print("\n"+40*'*')
    print("Formatting Products...")
    products = state["products"]
    formatted_result = formatProducts(products)
    state["products"] = formatted_result

    # Save products to MongoDB
    print("\n"+40*'*')
    print("Saving Products to the DB...")
    if state["products"]:
        save_products_to_db(state["products"], input_category)
    else:
        print("No products to save to the database.")

    return len(state["products"])
