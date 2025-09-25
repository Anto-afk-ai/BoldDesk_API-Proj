# mcp_blueprint.py
from flask import Blueprint, request, jsonify
from typing import Dict, List
from const.config import ITEMS
import uuid
import time

active_sessions: Dict[str, float] = {}
SESSION_TIMEOUT = 1800

def validate_session(session_id: str) -> bool:
    if session_id not in active_sessions:
        return False
    if time.time() - active_sessions[session_id] > SESSION_TIMEOUT:
        del active_sessions[session_id]
        return False
    # refresh timestamp on use (optional)
    active_sessions[session_id] = time.time()
    return True

def search_products(query: str) -> List[dict]:
    q = (query or "").lower()
    return [
        item for item in ITEMS
        if q in (item.get('name', '').lower()) or q in (item.get('category', '').lower())
    ]

mcp = Blueprint("mcp", __name__, url_prefix="/mcp")

@mcp.route("/session/open", methods=["POST"])
def session_open():
    try:
        body = request.get_json(force=True) or {}
    except Exception:
        return jsonify({"ok": False, "error": "invalid_json"}), 400

    session_id = body.get("session_id", str(uuid.uuid4()))
    active_sessions[session_id] = time.time()
    return jsonify({
        "ok": True,
        "session_id": session_id,
        "capabilities": {
            "context": ["products", "orders", "returns"],
            "tools": ["search_products", "check_order", "check_return_eligibility"]
        }
    }), 200

@mcp.route("/context/request", methods=["POST"])
def context_request():
    try:
        body = request.get_json(force=True) or {}
    except Exception:
        return jsonify({"type": "context.response", "request_id": None, "error": "invalid_json"}), 400

    session_id = body.get("session_id")
    request_id = body.get("request_id", str(uuid.uuid4()))
    resource = body.get("resource")

    if not session_id or not validate_session(session_id):
        return jsonify({"type": "context.response", "request_id": request_id, "error": "invalid_session"}), 401

    if resource == "products":
        return jsonify({"type": "context.response", "request_id": request_id, "data": ITEMS}), 200

    if resource == "orders":
        orders = [
            {"id": "ORD12345", "status": "Shipped", "customer": "Jane Doe"},
            {"id": "ORD12346", "status": "Processing", "customer": "John Smith"}
        ]
        return jsonify({"type": "context.response", "request_id": request_id, "data": orders}), 200

    return jsonify({"type": "context.response", "request_id": request_id, "error": "resource_not_found"}), 404

@mcp.route("/tool/run", methods=["POST"])
def tool_run():
    try:
        body = request.get_json(force=True) or {}
    except Exception:
        return jsonify({"type": "tool.result", "request_id": None, "error": "invalid_json"}), 400

    session_id = body.get("session_id")
    request_id = body.get("request_id", str(uuid.uuid4()))
    tool = body.get("tool")
    inputs = body.get("input", {})

    if not session_id or not validate_session(session_id):
        return jsonify({"type": "tool.result", "request_id": request_id, "error": "invalid_session"}), 401

    if tool == "search_products":
        results = search_products(inputs.get("q", ""))
        return jsonify({"type": "tool.result", "request_id": request_id, "output": results}), 200

    if tool == "check_order":
        order_id = inputs.get("order_id")
        if order_id == "ORD12345":
            return jsonify({
                "type": "tool.result",
                "request_id": request_id,
                "output": {"status": "Shipped", "estimated_delivery": "2025-09-20", "customer": "Jane Doe"}
            }), 200
        return jsonify({"type": "tool.result", "request_id": request_id, "error": "order_not_found"}), 404

    return jsonify({"type": "tool.result", "request_id": request_id, "error": "unknown_tool"}), 400

@mcp.route("/session/close", methods=["POST"])
def session_close():
    try:
        body = request.get_json(force=True) or {}
    except Exception:
        return jsonify({"ok": False, "error": "invalid_json"}), 400

    session_id = body.get("session_id")
    if session_id in active_sessions:
        del active_sessions[session_id]
        return jsonify({"ok": True}), 200
    return jsonify({"ok": False, "error": "session_not_found"}), 404