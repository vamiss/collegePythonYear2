from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import String, Integer, create_engine, Column

engine = create_engine("sqlite:///users.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    name = Column(String)

Base.metadata.create_all(bind=engine)

db = Session(autoflush=False, bind=engine)