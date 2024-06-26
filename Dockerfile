FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    rabbitmq-server \
    && apt-get clean \
    && pip install --no-cache-dir \
        pytesseract \
        celery

COPY . /app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
RUN pip install -e .

EXPOSE 8000

ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/

CMD ["celery", "worker", "-A", "tasks", "--loglevel=info"]
