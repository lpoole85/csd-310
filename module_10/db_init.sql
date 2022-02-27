

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE store (
    store_id       INT             NOT NULL       AUTO_INCREMENT,
    locale         VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id       INT             NOT NULL        AUTO_INCREMENT,
    book_name     VARCHAR(200)    NOT NULL,
    details       VARCHAR(500),
    author        VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id      INT             NOT NULL        AUTO_INCREMENT,
    first_name   VARCHAR(75)     NOT NULL,
    last_name    VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
); 

CREATE TABLE wishlist (
    wishlist_id   INT             NOT NULL        AUTO_INCREMENT,
    user_id       INT             NOT NULL,
    book_id       INT             NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id)
        REFERENCES user(user_id)
);

/* Create store location
*/
INSERT INTO store(locale)
    VALUES('123 Washington Avenue, New York City, NY 45348');

/* Create books
*/
INSERT INTO book(book_name, author, details) 
    VALUES('Harry Potter and the Sorcerers Stone', 'JK Rowling', 'Book Number One');

INSERT INTO book(book_name, author, details) 
    VALUES('Harry Potter and the Chamber of Secrets', 'JK Rowling', 'Book Number Two');

INSERT INTO book(book_name, author, details) 
    VALUES('Harry Potter and the Prisoner of Azkaban', 'JK Rowling', 'Book Number Three');

INSERT INTO book(book_name, author, details) 
    VALUES('Harry Potter and the Goblet of FIre', 'JK Rowling', 'Book Number Four');;

INSERT INTO book(book_name, author, details) 
    VALUES('Harry Potter and the Order of the Phoenix', 'JK Rowling', 'Book Number Five');;

INSERT INTO book(book_name, author, details) 
    VALUES('Harry Potter and the Half Blood Prince', 'JK Rowling', 'Book Number Six');;

INSERT INTO book(book_name, author, details) 
    VALUES('Harry Potter and the Deathly Hallows', 'JK Rowling', 'Book Number Seven');

INSERT INTO book(book_name, author, details) 
    VALUES('Fantastic Beasts and Where to Find Them', 'JK Rowling', 'A book about fantastic beasts');

INSERT INTO book(book_name, author, details) 
    VALUES('Quidditch Through the Ages', 'JK Rowling', 'A book on quidditch');

INSERT INTO book(book_name, author, details) 
    VALUES('The Tales of Beedle the Bard', 'JK Rowling', 'A book in the HP Series');

/* Create users
*/
INSERT INTO user(first_name, last_name) 
    VALUES('Harry', 'Potter');

INSERT INTO user(first_name, last_name)
    VALUES('Hermoine', 'Granger');

INSERT INTO user(first_name, last_name)
    VALUES('Ron', 'Weasley');

/* Create wishlist
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harry'), 
        (SELECT book_id FROM book WHERE book_name = 'Quidditch Through the Ages')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Hermoine'),
        (SELECT book_id FROM book WHERE book_name = 'Fantastic Beasts and Where to Find Them')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Ron'),
        (SELECT book_id FROM book WHERE book_name = 'The Tales of Beedle the Bard')
    );