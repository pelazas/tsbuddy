from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

def save_products_to_db(products):
    now = datetime.utcnow()
    client = MongoClient(MONGO_URL)
    db = client['tech_shopping_buddy']
    collection = db['products']
    for product in products:
        product["created_at"] = now
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
