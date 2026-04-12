FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY traffic-generator.py .

CMD ["python", "traffic-generator.py"]