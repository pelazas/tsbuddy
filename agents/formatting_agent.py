from agents import llm
import json

def run(state: dict):
    '''
    An agent that edits the values in state["products"], 
    formatting each attribute with its corresponding format, 
    so they are ready to be added to a Postgres database.

    Args:
        state (dict): The state dictionary containing the products to format.
                      Edits state["products"] in place.
        Returns: state (dict): The updated state dictionary with formatted products.
    '''

    system_message = """
        You are a formatting agent. Your task is to format the product information
        provided in the state["products"] list. The goal is to leave the products ready 
        to be added to a posgtreSQL db.
        Each product is a dictionary with the following keys:
        - "title": The product title
        - "price": The product price
        - "url": The product URL
        - "specs": The product specifications (optional)
        - "rating": The product rating (optional)
        - "rating_distribution": The product rating distribution (optional)
        - "score": The evaluation score
        - "explanation": The evaluation explanation

        I want you to convert the price and score to numbers,
        if rating distribution is present, convert it to a JSON string, if not, set it to None.
        The specs should be a JSON string, if not present, set it to None. In the specs remove the "Ver más" key if it exists.

        I want that the answer is only a JSON object with the full product formatted correclty.
        Do not include any other text or explanation.
    """

    for idx, product in enumerate(state["products"]):
        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": json.dumps(product, ensure_ascii=False, indent=2)
            }
        ]
        reply = llm.invoke(messages)
        try:
            result = json.loads(reply.content)
            state["products"][idx] = result
        except Exception as e:
            print("Error formatting product:", product)
            print("Raw reply:", reply.content)
            print("Exception:", e)

    return {"messages": [{"role": "assistant", "content": "Products formatted."}], "products": state["products"]}
