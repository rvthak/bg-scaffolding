INSERT OR IGNORE INTO users (id, email)
VALUES (1, 'maria.papadopoulou@gmail.com'),
       (2, 'nikos.georgiou@hotmail.com'),
       (3, 'elena.konstantinou@yahoo.com'),
       (4, 'dimitris.alexiou@gmail.com'),
       (5, 'sofia.nikolaou@outlook.com');

INSERT OR IGNORE INTO apartments (id, address, floor, description, owner)
VALUES (1, 'Ermou 14, Athens', '3rd', 'Cozy studio in the heart of Athens, close to Monastiraki', 1),
       (2, 'Kifisias 82, Kifisia', '1st', 'Bright 2-bedroom flat with garden view in a quiet neighborhood', 1),
       (3, 'Vouliagmenis 200, Glyfada', '5th', 'Modern apartment with sea view, 5 min walk to the beach', 2),
       (4, 'Mitropoleos 7, Thessaloniki', NULL, 'Ground floor loft near Aristotelous Square', 2),
       (5, 'Korinthou 33, Patras', '2nd', 'Spacious 3-bedroom apartment near the university', 3);

INSERT OR IGNORE INTO reservations (id, customer, apartment, start_date, end_date, created_at)
VALUES (1, 4, 1, '2025-03-01', '2025-03-07', '2025-02-10 10:23:00'),
       (2, 5, 1, '2025-03-15', '2025-03-20', '2025-02-12 14:05:00'),
       (3, 4, 3, '2025-04-01', '2025-04-10', '2025-03-01 09:00:00'),
       (4, 5, 2, '2025-04-05', '2025-04-12', '2025-03-10 18:45:00'),
       (5, 4, 5, '2025-05-01', '2025-05-05', '2025-04-01 11:30:00');