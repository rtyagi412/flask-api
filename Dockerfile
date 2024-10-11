FROM python:3.13-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Remove .pyc and __pycache__ files to clean up the build
RUN find . -type f -name '*.pyc' -delete && \
    find . -type d -name '__pycache__' -exec rm -r {} +

FROM python:3.13-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]