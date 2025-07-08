# agents/user_input_agent.py

import json
from agents import llm

def run(state: dict):
    if not state["search_results"]:
        return {"messages": [{"role": "assistant", "content": "No product to evaluate."}]}
    search_results = state["search_results"][-1]

    system_message = f"""
        You are a product evaluation agent. Your task is to analyze the information provided about a product and assign it an overall quality score from 1 to 10, where:

        - 1 means very poor quality or poor value,
        - 10 means excellent quality and outstanding value.

        I will provide you with a list of the products.

        Instructions:
        1. Consider the price relative to the specifications — better specs at a lower price should increase the score.
        2. Use the rating out of 5 as a major factor, but also analyze the rating distribution for possible skew (e.g., many low ratings might reduce confidence).
        3. Consider how strong the CPU and screen specs are relative to typical products in the category.
        4. If any specifications are missing or clearly low-end, adjust the score accordingly.
        5. Return only a JSON object with two keys: 
        - "score": an integer from 1 to 10
        - "explanation": a concise summary of the main reasons behind the score

        Example output:

        {{
        "score": 8,
        "explanation": "Good CPU model with high speed and sufficient cache, competitive price, rating of 4.2 with mostly positive reviews."
        }}
        """

    messages = [
        {"role": "system", "content": system_message},
        {
            "role": "user",
            "content": json.dumps(search_results, ensure_ascii=False, indent=2)  # <-- serialize to string
        }
    ]

    reply = llm.invoke(messages)

    return {"messages": [{"role": "assistant", "content": reply.content}]}
