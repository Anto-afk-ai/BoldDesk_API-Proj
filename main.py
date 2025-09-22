from flask import Flask, jsonify, render_template, send_from_directory
from waitress import serve

app = Flask(__name__, static_folder='build', template_folder='build')

# Simple API
@app.route('/api/fetch-product', methods=['GET'])
def fetch_product():
    products = {
        "product_count": 150,
        "active_bots": 25,
        "uptime": "99.9%"
    }
    return jsonify({"count": len(products), "products": products}), 200

# Serve React build and SPA fallback
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    try:
        if path:
            return send_from_directory('build', path)
    except Exception:
        pass
    return render_template('index.html')

if __name__ == '__main__':
    print("Server started")
    serve(app, host='0.0.0.0', port=8080)