from app.models import Documents, connect_db



session = connect_db()

documents = session.query(Documents).all()

for document in documents:
    print(document.id, '\t', document.file_path, '\t', document.date)



session.close()