FILE=/app/dblp.xml.gz
if [ ! -f "$FILE" ]; then
  wget -O /app/dblp.xml.gz https://dblp.org/xml/dblp.xml.gz
fi