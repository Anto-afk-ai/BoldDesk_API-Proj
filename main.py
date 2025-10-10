from flask import Blueprint, Flask, jsonify, render_template, send_from_directory, request
from const.config import ITEMS, ORDERS
from waitress import serve
from const.config import *
import flask_cors
from mcp_blueprint_new import mcp

API_KEY = "qqww22ttzxqwr6778"  # Change this to your desired key

app = Flask(__name__, static_folder='build', template_folder='build')
flask_cors.CORS(app)

api = Blueprint("api", __name__, url_prefix="/api")
order = Blueprint("order", __name__, url_prefix="/order")

def require_api_key():
    key = request.headers.get('X-API-KEY')
    return key == API_KEY

def check_api_key():
    if not require_api_key():
        return jsonify({'error': 'Invalid or missing API key'}), 401
    return None

# List all items
@api.route('/items', methods=['GET'])
def get_items():
    auth_resp = check_api_key()
    if auth_resp:
        return auth_resp
    return jsonify(ITEMS)

@app.route('/validate_user/<string:user_mail>', methods=['GET'])
def validate_user(user_mail):
    auth_resp = check_api_key()
    if auth_resp:
        return auth_resp
    if user_mail == "brianson.23@gmail.com":
        return jsonify({'status': 'User validated'})
    return jsonify({'status': 'User not recognized'}), 404

# Get item by id
@api.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    auth_resp = check_api_key()
    if auth_resp:
        return auth_resp
    for item in ITEMS:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Get order status
@order.route('/status', methods=['GET'])
def get_orderStatus():
    auth_resp = check_api_key()
    if auth_resp:
        return auth_resp
    item_id = request.args.get('item_id')
    if not item_id:
        return jsonify({'error': 'Missing item_id parameter'}), 400
    for item in ORDERS:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Order not found'}), 404

# Search items by name or category
@api.route('/items/search')
def search_items():
    check_api_key()
    q = request.args.get('q', '').lower()
    if not q:
        return jsonify({'error': 'Missing search query'}), 400
    results = [item for item in ITEMS if q in item['name'].lower() or q in item['category'].lower()]
    return jsonify(results)

@api.route('/key')
def kb():
    return API_KEY

api.register_blueprint(order)

app.register_blueprint(api)

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