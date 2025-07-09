# agents/user_input_agent.py

from agents import llm
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage


# Run function that receives the state and returns extracted structured info
def run(state: dict):
    user_input = state["messages"][-1]["content"]

    messages = [
        {
            "role": "system",
            "content": ( """
                You are a product assistant. Based on the user's input, 
                make a 1 line string query with the information needed to search for products. 
                Make it extremely concise, remove any unnecessary information
                """
            ),
        },
        {
            "role": "user",
            "content": user_input,
        },
    ]

    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}
