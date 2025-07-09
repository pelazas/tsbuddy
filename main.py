from flask import Flask, request, jsonify
from pipeline import run_pipeline

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    query = data.get('query')
    category = data.get('category')
    numberOfProducts = data.get('numberOfProducts')
    
    # Assuming run_pipeline returns the number of products added
    products_added = run_pipeline(query, category, numberOfProducts)
    
    return jsonify(message=f"{products_added} products added to the database.")

if __name__ == '__main__':
    app.run(debug=True)
