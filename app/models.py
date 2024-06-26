from datetime import date

from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.orm import Session, relationship, sessionmaker
from sqlalchemy.orm import declarative_base

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())
    return session


class Documents(Base):
    __tablename__ = 'Documents'
    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String)
    date = Column(Date)


class Documents_text(Base):
    __tablename__ = 'Documents_text'
    id = Column(Integer, primary_key=True, index=True)
    id_doc = Column(Integer, ForeignKey('Documents.id'))
    text = Column(String)



def main():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
