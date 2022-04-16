GRANT ALL ON *.* TO 'khiemle'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS dblp_database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS articles(
  id INT NOT NULL AUTO_INCREMENT,
  address TEXT,
  author TEXT,
  booktitle TEXT,
  cdrom TEXT,
  chapter TEXT,
  cite TEXT,
  crossref TEXT,
  editor TEXT,
  ee TEXT,
  isbn TEXT,
  journal TEXT,
  month TEXT,
  note TEXT,
  number TEXT,
  pages TEXT,
  publisher TEXT,
  publnr TEXT,
  school TEXT,
  series TEXT,
  title TEXT,
  url TEXT,
  volume TEXT,
  year TEXT,
  PRIMARY KEY (id)
);