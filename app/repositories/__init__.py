from sqlalchemy.orm import sessionmaker
from app.config.database import engine

Session = sessionmaker(bind=engine)
session = Session()