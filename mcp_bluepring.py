# mcp_blueprint.py
from flask import Blueprint, request, jsonify

mcp = Blueprint("mcp", __name__, url_prefix="/mcp")

# session open
@mcp.route("/session/open", methods=["POST"])
def session_open():
    body = request.get_json() or {}
    session_id = body.get("session_id", "demo-session")
    return jsonify({"ok": True, "session_id": session_id}), 200

# context request
@mcp.route("/context/request", methods=["POST"])
def context_request():
    body = request.get_json() or {}
    request_id = body.get("request_id", "req-demo")
    resource = body.get("resource")
    # return canned response for demo
    if resource == "products":
        data = [
            {"id": "p1", "name": "Demo A"},
            {"id": "p2", "name": "Demo B"}
        ]
        return jsonify({"type": "context.response", "request_id": request_id, "data": data}), 200
    return jsonify({"type": "context.response", "request_id": request_id, "error": "resource_not_found"}), 404

# tool run
@mcp.route("/tool/run", methods=["POST"])
def tool_run():
    body = request.get_json() or {}
    request_id = body.get("request_id", "tool-demo")
    tool = body.get("tool")
    inputs = body.get("input")
    if tool == "search_products":
        q = (inputs or {}).get("q", "").lower()
        results = [p for p in [{"id":"p1","name":"Demo A"},{"id":"p2","name":"Demo B"}] if q in p["name"].lower()]
        return jsonify({"type": "tool.result", "request_id": request_id, "output": results}), 200
    return jsonify({"type": "tool.result", "request_id": request_id, "error": "unknown_tool"}), 400