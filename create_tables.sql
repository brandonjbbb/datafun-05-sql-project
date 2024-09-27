CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birthdate TEXT
);

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    published_year INTEGER,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
