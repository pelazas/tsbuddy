
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

class Product(BaseModel):
    """Product to be searched for"""
    product_category: str = Field(description="Product category")
    desired_features: str = Field(description="Desired features")
    budget_range: str = Field(description="Budget range")
    constraints: str = Field(description="Constraints")

# llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
# structured_llm = llm.with_structured_output(Product)

def get_product_category(user_query: str):
    """
    Get the product category from the user query.
    """
    # return structured_llm.invoke(user_query)
    return {
        "product_category": "headphones",
        "desired_features": "noise cancelling",
        "budget_range": "under 200€",
        "constraints": "battery life > 10h"
    }
