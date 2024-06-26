import os
import uuid

from datetime import datetime
from fastapi import APIRouter, File, UploadFile, Depends, Path, HTTPException
from fastapi.responses import JSONResponse
from app.models import connect_db, Documents, Documents_text
from sqlalchemy.orm import Session
from app.tasks import analyse


UPLOAD_DIR = 'documents'
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()


@router.post('/upload_doc', name='upload:doc')
async def upload_doc(
        file: UploadFile = File(...),
        database: Session = Depends(connect_db)
):
    try:
        file_extension = file.filename.split('.')[-1]
        file_name = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, "wb") as f:
            contents = await file.read()
            f.write(contents)

        new_document = Documents(
            file_path=file_path,
            date=datetime.now().date()
        )
        database.add(new_document)
        database.commit()

        return JSONResponse(content={"filename": file_name}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)


@router.delete('/doc_delete/{file_id}', name='delete:doc')
def delete_doc(
        file_id: int = Path(..., title="Это ID файла, который вы хотите удалить."),
        database: Session = Depends(connect_db)
):
    del_file = database.query(Documents).filter(Documents.id == file_id).first()

    if not del_file:
        raise HTTPException(status_code=404, detail="File not found")

    try:
        os.remove(del_file.file_path)

        database.delete(del_file)
        database.commit()
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/doc_analyse/{file_id}', name='analyse:doc')
def analyse_doc(
        file_id: int = Path(..., title="Это ID файла, который вы хотите преобразовать"),
):
    task = analyse(file_id)

@router.get('/get_text/{file_id}', name='get:doc')
def get_text(
        file_id: int = Path(..., title="Это ID файла, которы вы хотите получить"),
        database: Session = Depends(connect_db)
):
    get_file = database.query(Documents_text).filter(Documents_text.id == file_id).first()

    if not get_file:
        raise  HTTPException(status_code=404, detail="File not found")

    return get_file


