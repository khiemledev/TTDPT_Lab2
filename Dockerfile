FROM python:3.9

WORKDIR /app

RUN python3 -m pip install --upgrade pip

RUN pip install "uvicorn[standard]" fastapi cryptography pymysql xmltodict

COPY ./app .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
