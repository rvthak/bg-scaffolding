import logging
from flask import Flask, jsonify
from .service import Service
from .errors import NotFoundError

app = Flask(__name__)
_service = Service()

logger = logging.getLogger(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/items")
def list_items():
    items = _service.get_all()
    return jsonify([{"id": item.id, "name": item.name} for item in items])


@app.get("/items/<int:item_id>")
def get_item(item_id: int):
    item = _service.get_by_id(item_id)
    return jsonify({"id": item.id, "name": item.name})


@app.errorhandler(NotFoundError)
def handle_not_found(e):
    return jsonify({"error": str(e)}), 404


@app.errorhandler(Exception)
def handle_unexpected(e):
    logger.exception("Unhandled error")
    return jsonify({"error": "internal server error"}), 500
