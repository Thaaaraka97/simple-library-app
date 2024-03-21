FROM python:3.11-alpine

WORKDIR /app

COPY api_gateway.py /app/api_gateway.py
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 5002

CMD ["python","api_gateway.py"]