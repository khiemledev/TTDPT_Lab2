import xmltodict
import json
from collections import OrderedDict
from pathlib import Path
from gzip import GzipFile
from utils import get_connection

total_inserted = 0


def main():
    global total_inserted

    table_fields = ['author', 'editor', 'title', 'booktitle', 'pages', 'year', 'address', 'journal', 'volume', 'number', 'month',
                    'url', 'ee', 'cdrom', 'cite', 'publisher', 'note', 'crossref', 'isbn', 'series', 'school', 'chapter', 'publnr']

    file_path = Path("dblp.xml.gz")
    if not file_path.exists():
        raise FileNotFoundError()

    print("Start importing")

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:

                def handle_item(_, element):
                    global total_inserted
                    record = {k: "" for k in table_fields}

                    for key in element.keys():
                        if key in record:
                            sub_ele = element[key]
                            if isinstance(sub_ele, str):
                                record[key] = sub_ele
                            elif isinstance(sub_ele, list):
                                record[key] = json.dumps(sub_ele)
                            elif isinstance(sub_ele, OrderedDict):
                                tmp = {
                                    "type": "",
                                    "label": "",
                                    "text": "",
                                }
                                if "@type" in sub_ele:
                                    tmp["type"] = sub_ele["@type"]
                                if "@label" in sub_ele:
                                    tmp["label"] = sub_ele["@label"]
                                if "#text" in sub_ele:
                                    tmp["text"] = sub_ele["#text"]
                                record[key] = json.dumps(tmp)

                    sql = '''
                        INSERT INTO articles(
                            author, editor, title, booktitle, pages,
                            year, address, journal, volume, number,
                            month, url, ee, cdrom, cite,
                            publisher, note, crossref, isbn, series,
                            school, chapter, publnr
                        ) VALUES(
                            "%s", "%s", "%s", "%s", "%s",
                            "%s", "%s", "%s", "%s", "%s",
                            "%s", "%s", "%s", "%s", "%s",
                            "%s", "%s", "%s", "%s", "%s",
                            "%s", "%s", "%s"
                        );
                    '''
                    cursor.execute(sql, tuple(record[k] for k in table_fields))
                    print(f"Item {total_inserted} inserted")
                    total_inserted += 1

                    return True

                xml_file = GzipFile(str(file_path))
                xmltodict.parse(
                    xml_file,
                    item_depth=2,
                    item_callback=handle_item,
                )
                print("Total inserted items:", total_inserted)

            connection.commit()
    except Exception as err:
        print(str(err))


if __name__ == "__main__":
    main()
