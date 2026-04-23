CREATE TABLE IF NOT EXISTS users
(
    id    INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS apartments
(
    id          INTEGER PRIMARY KEY,
    address     TEXT    NOT NULL,
    floor       TEXT,
    description TEXT,
    owner       INTEGER NOT NULL REFERENCES users (id)
);


CREATE TABLE IF NOT EXISTS reservations
(
    id         INTEGER PRIMARY KEY,
    customer   INTEGER NOT NULL REFERENCES users (id),
    apartment  INTEGER NOT NULL REFERENCES apartments (id),
    start_date DATE    NOT NULL,
    end_date   DATE    NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        CHECK (end_date > start_date)
);

CREATE INDEX idx_reservations_apt_dates ON reservations(apartment, start_date, end_date);