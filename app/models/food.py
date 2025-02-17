from sqlalchemy import Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    portion_size = Column(Float) # grams
    portion_unit = Column(String) # g, ml, etc.

    # Macronutrients
    calories = Column(Float)
    proteins = Column(Float)
    carbohydrates = Column(Float)
    fats = Column(Float)

    # Additional information as micronutrients
    nutritional_info = Column(JSON)

    # Metadata
    brand = Column(String, nullable=True)
    source = Column(String) # Information source
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())