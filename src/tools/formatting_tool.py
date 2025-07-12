import re
import json
from datetime import datetime

def parse_price(price_str):
    if not price_str:
        return None
    # Remove currency symbols and spaces, replace comma with dot
    price_num = re.sub(r"[^\d,\.]", "", price_str).replace(",", ".")
    try:
        return float(price_num)
    except ValueError:
        return None

def parse_specs(specs_str):
    if not specs_str:
        return None
    # Remove "Ver más" and split into lines
    specs_str = specs_str.replace("Ver más", "").strip()
    lines = [line for line in specs_str.split("\n") if line.strip()]
    specs = {}
    for line in lines:
        if "\t" in line:
            key, value = line.split("\t", 1)
            specs[key.strip()] = value.strip()
    return specs if specs else None

def extract_brand_and_model(specs):
    """Extract brand and model from specs dictionary"""
    if not specs:
        return None, None
    
    brand = specs.get("Marca", None)
    model = None
    
    # Look for model with different possible keys
    for key in specs.keys():
        if key == "Modelo" or key == "Nombre del modelo" or key.startswith("Modelo"):
            model = specs[key]
            break
    
    return brand, model

def parse_rating_distribution(rating_dist_str):
    if not rating_dist_str:
        return None
    lines = [line for line in rating_dist_str.split("\n") if line.strip()]
    dist = {}
    i = 0
    while i < len(lines) - 1:
        label = lines[i].strip()
        value = lines[i+1].strip().replace('\xa0', ' ')
        dist[label] = value
        i += 2
    # Check if all values are 0%
    if all(v.replace(" ", "") in ("0%", "0") for v in dist.values()):
        return None
    return dist if dist else None

def parse_score(score):
    try:
        return float(score)
    except Exception:
        return None

def formatProducts(products: list):

    formatted_products = []

    for idx, product in enumerate(products):
        specs = parse_specs(product.get("specs"))
        brand, model = extract_brand_and_model(specs)
        today = datetime.utcnow().strftime("%Y-%m-%d")
        
        formatted = {
            "title": product.get("title"),
            "price": parse_price(product.get("price")),
            "url": product.get("url"),
            "specs": json.dumps(specs) if specs else None,
            "brand": brand,
            "model": model,
            "rating": product.get("rating"),
            "rating_distribution": json.dumps(parse_rating_distribution(product.get("rating_distribution"))) if product.get("rating_distribution") else None,
            "score": parse_score(product.get("score")),
            "explanation": product.get("explanation"),
            "n_reviews": product.get("n_reviews"),
            "image_url": product.get("image_url"),
            "previous_prices": product.get("previous_prices", {}) or {today: product.get("price")},
        }
        formatted_products.append(formatted)
    return formatted_products
