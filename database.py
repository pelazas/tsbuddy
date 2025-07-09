from pymongo import MongoClient
from datetime import datetime

def save_products_to_db(products):
    now = datetime.utcnow()
    for product in products:
        product["created_at"] = now
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tech_shopping_buddy']
    collection = db['products']
    collection.insert_many(products)
    client.close()
