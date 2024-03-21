FROM python:3.11-alpine

WORKDIR /app

COPY web_frontend.py /app/web_frontend.py
COPY templates/ /app/templates
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5003

CMD ["python","web_frontend.py"]