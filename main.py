from agents import user_input_agent
from agents.evaluation_agent import run as evaluation_run
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from scrapers import scrape_products

class State(TypedDict):
    messages: Annotated[list, add_messages]
    search_results: list

def run_pipeline():
    user_input = input("Describe what you're looking for:\n> ")

    # 1. Initialize state
    state: State = {
        "messages": [{"role": "user", "content": user_input}],
        "search_results": [],
    }

    # 2. User Input Agent with the user's query
    user_query_result = user_input_agent.run(state)
    state["messages"].extend(user_query_result["messages"])

    # 3. Call the run method in scrape_products.py with the parsed query, store the search_results in the state
    parsed_query = state["messages"][-1]["content"]
    search_results = scrape_products.run(parsed_query)
    state["search_results"].append(search_results)

    # 4. Call the Evaluation agent with the state, print the evaluation results
    # We'll evaluate the first product as an example
    if search_results and len(search_results) > 0 and search_results[0]:
        eval_state = state.copy()
        # Pass the first product (dict) as a single-item list
        eval_state["search_results"] = [search_results[0]]
        evaluation_result = evaluation_run(eval_state)
        print("Evaluation Result:")
        print(evaluation_result["messages"][0]["content"])
    else:
        print("No products found.")

if __name__ == "__main__":
    run_pipeline()