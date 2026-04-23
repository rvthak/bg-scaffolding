from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional


@dataclass
class User:
    id: int
    email: str


@dataclass
class Apartment:
    id: int
    address: str
    owner: int
    floor: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Reservation:
    id: int
    customer: str
    apartment: int
    start_date: date
    end_date: date
    created_at: datetime
