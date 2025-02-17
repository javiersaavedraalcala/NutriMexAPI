from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.food import Food
from app.schemas.food import FoodCreate, FoodUpdate


def get_food(db: Session, food_id: int) -> Optional[Food]:
    """Get food by ID"""
    return db.query(Food).filter(Food.id == food_id).first()


def get_foods(
        db: Session,
        skip: int = 0,
        limit: int = 100
) -> List[Food]:
    """Get food list with pagination"""
    return db.query(Food).offset(skip).limit(limit).all()


def get_foods_by_category(
        db: Session,
        category: str,
        skip: int = 0,
        limit: int = 100
) -> List[Food]:
    """Get food by category"""
    return db.query(Food).filter(Food.category == category).offset(skip).limit(limit).all()

def create_food(db: Session, food: FoodCreate) -> Food:
    """Create a new food"""
    db_food = Food(**food.model_dump())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def update_food(
        db: Session,
        food_id: int,
        food: FoodUpdate
) -> Optional[Food]:
    """Update an existing food"""
    db_food = get_food(db, food_id)
    if db_food:
        food_data = food.model_dump(exclude_unset=True)
        for key, value in food_data.items():
            setattr(db_food, key, value)
        db.commit()
        db.refresh(db_food)
    return db_food

def delete_food(db: Session, food_id: int) -> Optional[Food]:
    """Delete food item"""
    db_food = get_food(db, food_id)
    if db_food:
        db.delete(db_food)
        db.commit()
    return db_food










