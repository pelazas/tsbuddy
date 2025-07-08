# agents/user_input_agent.py

from agents import llm
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage


# Define output schema for the LLM
class UserQuery(BaseModel):
    category: str = Field(..., description="Product category")
    features: list[str] = Field(..., description="Desired features")
    budget: str = Field(..., description="Budget range, like 'under $500' or '100-300€'")
    constraints: list[str] = Field(..., description="Technical constraints like 'battery > 10h'")


# Run function that receives the state and returns extracted structured info
def run(state: dict):
    user_input = state["messages"][-1]["content"]

    schema_llm = llm.with_structured_output(UserQuery)

    result = schema_llm.invoke([
        {
            "role": "system",
            "content": """You are a product assistant. Extract the following fields from the user request:
            - category (e.g. 'laptop', 'smartphone')
            - features (desired features)
            - budget (price range)
            - constraints (technical requirements)
            Format the output strictly in structured JSON."""
        },
        HumanMessage(content=user_input)
    ])

    return {**state, "parsed_query": result.model_dump()}
