from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute(text("""create table documents (id INTEGER NOT NULL PRIMARY KEY,
        file_path TEXT,
        date DATE)
    """))

    session.execute(text("""create table documents_txt (id INTEGER NOT NULL PRIMARY KEY,
        id_doc INTEGER,
        text TEXT,
        FOREIGN KEY (id_doc) REFERENCES documents(id))
    """))

    session.close()

if __name__ == '__main__':
    main()
