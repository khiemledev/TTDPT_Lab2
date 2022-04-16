ALTER TABLE articles ADD FULLTEXT INDEX text_search_1(
  author,
  editor,
  title,
  booktitle,
  pages,
  year,
  address
);

ALTER TABLE articles ADD FULLTEXT INDEX text_search_2(
  journal,
  volume,
  number,
  month,
  url,
  ee,
  cdrom
);

ALTER TABLE articles ADD FULLTEXT INDEX text_search_3(
  cite,
  publisher,
  note,
  crossref,
  isbn,
  series,
  school,
  chapter,
  publnr
);