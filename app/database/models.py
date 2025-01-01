from sqlalchemy import Column, String, DateTime, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.db import Base
from uuid import uuid4

class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    gender = Column(String(1), nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=False)
    address = Column(String, nullable=True)
    postal_code = Column(String(30), nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    profession = Column(String, nullable=True)
    company = Column(String, nullable=True)
    language = Column(String, nullable=True)
    marrital_status = Column(Boolean, nullable=False)
    date_generated = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now())

    
    sales = relationship("SalesModel", back_populates="user")
    feedbacks = relationship("FeedbackModel", back_populates="user")
    campaigns = relationship("MarketingCampaignModel", back_populates="user")

class SalesModel(Base):
    __tablename__ = "sales"

    transaction_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    product_id = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False, default=1)
    price_per_unit = Column(Float, nullable=False)
    discount_percentage = Column(Float, nullable=True, default=0)
    discount_value = Column(Float, nullable=True, default=0)
    total_value = Column(Float, nullable=False)
    sale_date = Column(DateTime, nullable=False)
    payment_method = Column(String, nullable=False)
    store_location = Column(String, nullable=True)
    region = Column(String, nullable=True)
    shipping_cost = Column(Float, nullable=True)
    delivery_time_days = Column(Integer, nullable=True)
    customer_feedback = Column(String, nullable=True)

    
    user = relationship("UserModel", back_populates="sales")
    shipping = relationship("ShippingModel", back_populates="sale")
    feedback = relationship("FeedbackModel", back_populates="sale")

class ShippingModel(Base):
    __tablename__ = "shipping"

    shipping_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    transaction_id = Column(String, ForeignKey("sales.transaction_id"), nullable=False)
    carrier = Column(String, nullable=False)
    shipping_method = Column(String, nullable=False)
    shipping_cost = Column(Float, nullable=False)
    delivery_time_days = Column(Integer, nullable=False)
    delivery_status = Column(String, nullable=False)

    sale = relationship("SalesModel", back_populates="shipping")

class FeedbackModel(Base):
    __tablename__ = "feedbacks"

    feedback_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    transaction_id = Column(String, ForeignKey("sales.transaction_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    feedback_text = Column(String, nullable=True)
    feedback_rating = Column(Integer, nullable=True)  # De 1 a 5, por exemplo.

    user = relationship("UserModel", back_populates="feedbacks")
    sale = relationship("SalesModel", back_populates="feedback")

class MarketingCampaignModel(Base):
    __tablename__ = "marketing_campaigns"

    campaign_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    campaign_name = Column(String, nullable=False)
    campaign_date = Column(DateTime, default=func.now())
    campaign_type = Column(String, nullable=False)

    user = relationship("UserModel", back_populates="campaigns")

class ProductModel(Base):
    __tablename__ = "products"

    product_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    product_name = Column(String, nullable=False)
    category_id = Column(String, ForeignKey("categories.category_id"), nullable=False)
    price_per_unit = Column(Float, nullable=False)
    brand = Column(String, nullable=True)

    category = relationship("CategoryModel", back_populates="products")

class CategoryModel(Base):
    __tablename__ = "categories"

    category_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    category_name = Column(String, nullable=False)

    products = relationship("ProductModel", back_populates="category")