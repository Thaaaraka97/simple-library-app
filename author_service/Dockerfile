FROM python:3.11-alpine

WORKDIR /app

COPY author_service.py /app/author_service.py
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 5001

CMD ["python","author_service.py"]