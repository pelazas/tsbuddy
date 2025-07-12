from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

def save_products_to_db(products, category):
    now = datetime.utcnow()
    client = MongoClient(MONGO_URL)
    db = client['tech_shopping_buddy']
    collection = db['products']
    for product in products:
        product["created_at"] = now
        product["category"] = category
        existing = collection.find_one({"title": product["title"]})
        if existing:
            # Update the existing document with new data
            collection.update_one(
                {"_id": existing["_id"]},
                {"$set": product}
            )
        else:
            # Insert as new document
            collection.insert_one(product)
    client.close()

def product_exists(product):
    client = MongoClient(MONGO_URL)
    db = client['tech_shopping_buddy']
    collection = db['products']

    title = product.get("title")
    brand = product.get("brand")
    model = product.get("model")
    price = product.get("price")
    today = datetime.utcnow().strftime("%Y-%m-%d")

    existing = None
    if title:
        existing = collection.find_one({"title": title})
    elif brand and model:
        existing = collection.find_one({"brand": brand, "model": model})

    if existing:
        # Update fields with new product data
        update_fields = product.copy()
        # Handle previous_prices
        previous_prices = existing.get("previous_prices", {})
        previous_prices[today] = price
        update_fields["previous_prices"] = previous_prices
        collection.update_one(
            {"_id": existing["_id"]},
            {"$set": update_fields}
        )
        client.close()
        return True

    client.close()
    return False
