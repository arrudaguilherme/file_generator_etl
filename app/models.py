from sqlalchemy import Column, String, DateTime, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
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

    sales = relationship("SalesModel", back_populates="user")

class SalesModel(Base):
    __tablename__ = "sales"

    transaction_id = Column(String, primary_key=True, index=True) 
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False) 
    product_id = Column(String, nullable=False) 
    product_name = Column(String, nullable=False) 
    category = Column(String, nullable=True) 
    brand = Column(String, nullable=True) 
    quantity = Column(Integer, nullable=False, default=1) 
    price_per_unit = Column(Float, nullable=False) 
    discount_percentage = Column(Float, nullable=True, default=0) 
    discount_value = Column(Float, nullable=True, default=0) 
    total_value = Column(Float, nullable=False) 
    sale_date = Column(DateTime,nullable=False) 
    payment_method = Column(String, nullable=False) 
    store_location = Column(String, nullable=True) 
    region = Column(String, nullable=True) 
    shipping_cost = Column(Float, nullable=True) 
    delivery_time_days = Column(Integer, nullable=True) 
    customer_feedback = Column(String, nullable=True) 

    user = relationship("Usermodel", back_populates="sales")