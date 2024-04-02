FROM python:3.11-alpine

WORKDIR /app

COPY book_service.py /app/book_service.py
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","book_service.py"]