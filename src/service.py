import logging
from .models import Item
from .errors import NotFoundError
from . import store

logger = logging.getLogger(__name__)


class Service:
    def get_all(self) -> list[Item]:
        return store.get_all()

    def get_by_id(self, item_id: int) -> Item:
        item = store.get_by_id(item_id)
        if item is None:
            raise NotFoundError(f"Item {item_id} not found")
        return item

    def reset(self) -> None:
        store.reset()
