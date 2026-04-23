import logging
from datetime import date

from . import store

logger = logging.getLogger(__name__)


class Service:

    @staticmethod
    def check_apartment_availability(apartment_id: int, start_date: date, end_date: date):
        is_available = store.is_apartment_available(apartment_id, start_date, end_date)
        available_apartments = store.get_available_apartments(start_date, end_date)
        return is_available, available_apartments
