from fastapi import FastAPI
from utils import get_connection
from typing import Optional

app = FastAPI()


@app.get("/")
def home():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT id FROM articles WHERE id=1;"
                cursor.execute(sql)
            connection.commit()
        return {
            "database_status": "Ready",
        }
    except Exception as err:
        return {
            "database_status": "Error",
            "error": str(err),
        }


@app.get("/search")
def search(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[str] = None,
    address: Optional[str] = None,
    booktitle: Optional[str] = None,
    pages: Optional[str] = None,
):
    if title is None and\
            author is None and\
            year is None and\
            address is None and\
            booktitle is None and\
            pages is None:
        return {
            "status": "Error",
            "message": "No query specified"
        }

    queries = []
    if title:
        queries.append(title)
    if author:
        queries.append(author)
    if year:
        queries.append(year)
    if address:
        queries.append(address)
    if booktitle:
        queries.append(booktitle)
    if pages:
        queries.append(pages)
    queries = " ".join(queries)

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql = '''SELECT id FROM articles WHERE MATCH(
                        author,
                        editor,
                        title,
                        booktitle,
                        pages,
                        year,
                        address
                ) AGAINST("%s") LIMIT 0, 100;'''
                cursor.execute(sql, (queries))
                data = cursor.fetchmany(100)
                return {
                    "status": "Success",
                    "data": data,
                }
    except Exception as err:
        return {
            "status": "Error",
            "message": str(err),
        }


@app.get("/detailed/{id}")
def get_detailed(
    id: str,
):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM articles WHERE id=%s;"
                cursor.execute(sql, (id))
                data = cursor.fetchone()
                return {
                    "status": "Success",
                    "data": data,
                }
    except Exception as err:
        return {
            "status": "Error",
            "message": str(err),
        }
