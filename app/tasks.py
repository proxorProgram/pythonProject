from celery import shared_task
from pytesseract import image_to_string
from app.models import Documents, Documents_text, SessionLocal
from sqlalchemy.orm import Session
from celery import Celery
from PIL import Image


celery_app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672//')

@shared_task
def analyse(file_id, database: Session = SessionLocal()):
    try:
        doc_analyse = database.query(Documents).filter(Documents.id == file_id).first()
        if doc_analyse:
            with Image.open(doc_analyse.file_path) as f:
                ready_doc = image_to_string(f)

            new_document = Documents_text(id_doc=doc_analyse.id, text=ready_doc)
            database.add(new_document)
            database.commit()
            return new_document.text
        else:
            return None
    finally:
        database.close()


