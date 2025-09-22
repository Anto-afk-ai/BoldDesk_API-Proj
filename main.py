from flask import Flask, jsonify, render_template, send_from_directory, request
from const.config import ITEMS
from waitress import serve
from const.config import *
import flask_cors


API_KEY = "qqww22ttzxqwr6778"  # Change this to your desired key

app = Flask(__name__, static_folder='build', template_folder='build')
flask_cors.CORS(app)

# Order Status API
# Order Status API

def require_api_key():
    key = request.headers.get('X-API-KEY')
    if key != API_KEY:
        return False
    return True

def check_api_key():
    if not require_api_key():
        return jsonify({'error': 'Invalid or missing API key'}), 401
    
# List all items
@app.route('/api/items')
def get_items():
    check_api_key()
    return jsonify(ITEMS)

# Get item by id
@app.route('/api/items/<int:item_id>')
def get_item(item_id):
    check_api_key()
    for item in ITEMS:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Search items by name or category
@app.route('/api/items/search')
def search_items():
    check_api_key()
    q = request.args.get('q', '').lower()
    results = [item for item in ITEMS if q in item['name'].lower() or q in item['category'].lower()]
    return jsonify(results)

# Returns API
@app.route('/api/returns')
def returns():
    from flask import request
    order_id = request.args.get('orderId')
    if not order_id:
        return jsonify({'error': 'Missing orderId'}), 400
    if order_id == 'ORD12346':
        return jsonify({
            'orderId': order_id,
            'returnEligible': True,
            'reason': 'Within 30 days',
            'instructions': 'Use the prepaid label to return your item.'
        })
    return jsonify({'error': 'Order not found or not eligible for return'}), 404

# Refunds API
@app.route('/api/refunds')
def refunds():
    from flask import request
    order_id = request.args.get('orderId')
    if not order_id:
        return jsonify({'error': 'Missing orderId'}), 400
    if order_id == 'ORD12347':
        return jsonify({
            'orderId': order_id,
            'refundStatus': 'Pending',
            'amount': 49.99,
            'method': 'Original payment method'
        })
    return jsonify({'error': 'Order not found or not eligible for refund'}), 404

# FAQ API
@app.route('/api/faq')
def faq():
    return jsonify([
        { 'q': 'How do I track my order?', 'a': 'Use the order status page.' },
        { 'q': 'How do I request a return?', 'a': 'Go to your orders and select return.' }
    ])

# Knowledge Base API
@app.route('/api/key')
def kb():
    return API_KEY

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