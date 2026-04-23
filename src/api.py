import logging
from datetime import date

from flask import Flask, jsonify, request

from .service import Service
from .errors import ValidationError

app = Flask(__name__)
_service = Service()

logger = logging.getLogger(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/apartments/<int:apartment_id>/availability")
def get_apartment_availability(apartment_id: int):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    start_date, end_date = validate_period(start_date, end_date)

    is_available, alternatives = _service.check_apartment_availability(apartment_id, start_date, end_date)

    return jsonify({"is_available": is_available,
                    "alternatives": [{"id": ap.id, "address": ap.address} for ap in alternatives]})


def validate_period(start_date, end_date):
    if not start_date or not end_date:
        raise ValidationError("start_date and end_date are required")

    try:
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
    except ValueError:
        raise ValidationError("dates must be in YYYY-MM-DD format")

    if start_date >= end_date:
        raise ValidationError("start_date must be before end_date")

    return start_date, end_date


@app.errorhandler(ValidationError)
def handle_validation(e):
    return jsonify({"error": str(e)}), 400


@app.errorhandler(Exception)
def handle_unexpected(e):
    logger.exception("Unhandled error", exc_info=e)
    return jsonify({"error": "internal server error"}), 500
