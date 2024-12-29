from sqlalchemy import Column, String, DateTime, Integer, Boolean
from sqlalchemy.sql import func
from database import Base

class UserModel(Base):
    __tablename__ = "users"
    user_id = Column(Integer,primary_key=True, index= True)
    name = Column(String,nullable=False) 
    birth_date = Column(DateTime,nullable=False) 
    gender = Column(String(1),nullable=False) 
    phone_number = Column(String(),nullable=True) 
    email = Column(String,nullable=False) 
    address = Column(String,nullable=True) 
    postal_code = Column(String(30),nullable=True) 
    city = Column(String,nullable=True) 
    state = Column(String,nullable=True) 
    country = Column(String,nullable=True) 
    profession = Column(String,nullable=True) 
    company = Column(String,nullable=True) 
    language = Column(String,nullable=True) 
    marrital_status = Column(Boolean,nullable=False) 
    date_generated = Column(DateTime,nullable=False)
    created_at = Column(DateTime, default=func.now()) 