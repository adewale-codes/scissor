from sqlalchemy import Column, Integer, String
from app.db.database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, index=True)
    short_url = Column(String, index=True, unique=True)
    custom_alias = Column(String, index=True, nullable=True)
    click_count = Column(Integer, default=0) 
