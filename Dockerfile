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
RUN pip install -e .


ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
