from pymongo import MongoClient

def save_products_to_db(products):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['tech_shopping_buddy']
    collection = db['products']
    collection.insert_many(products)
    client.close()
