
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
from langchain_core.messages import BaseMessage

from agents.user_input_agent import get_product_category

class AgentState(TypedDict):
    user_query: str
    product: dict
    report: str

def user_input_node(state):
    product = get_product_category(state["user_query"])
    return {"product": product}

def search_node(state):
    # Placeholder for the search agent
    print("Searching for products...")
    return {"report": ""}

workflow = StateGraph(AgentState)

workflow.add_node("user_input", user_input_node)
workflow.add_node("search", search_node)

workflow.set_entry_point("user_input")

workflow.add_edge("user_input", "search")
workflow.add_edge("search", END)

app = workflow.compile()

if __name__ == "__main__":
    inputs = {"user_query": "best noise cancelling headphones under 200€"}
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---")
