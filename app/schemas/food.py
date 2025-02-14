from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

# Basic schema with common fields
class FoodBase(BaseModel):
    name: str
    category: str
    portion_size: float = Field(gt=0)
    portion_unit: str
    calories: float = Field(ge=0)
    proteins: float = Field(ge=0)
    carbohydrates: float = Field(ge=0)
    fats: float = Field(ge=0)
    nutritional_info: Dict = Field(default_factory=dict)
    brand: Optional[str] = None
    source: str

# Schema to create new food
class FoodCreate(FoodBase):
    pass

# Schema to update food
class FoodUpdate(FoodBase):
    pass

# Schema for responses (include ID and timestamps)
class Food(FoodBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True  # Allows conversion from sqlalchemy to pydantic