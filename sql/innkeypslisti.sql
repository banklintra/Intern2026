-- Ein innkeypslisti til SQL-avbjóðingarnar. Prísirnir eru bara dømi.
CREATE TABLE item (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name   TEXT    NOT NULL,
    amount INTEGER NOT NULL,
    price  INTEGER NOT NULL
);

INSERT INTO item (name, amount, price) VALUES
    ('Pizza',    2, 45),
    ('Chips',    3, 20),
    ('Cola',     4, 15),
    ('Snickers', 5, 10),
    ('Ís',       1, 35),
    ('Popcorn',  2, 12),
    ('Bananir',  6, 3),
    ('Mjólk',    1, 18),
    ('Breyð',    1, 25),
    ('Ostur',    1, 45);
