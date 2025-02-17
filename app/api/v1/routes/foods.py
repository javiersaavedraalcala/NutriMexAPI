from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.config import settings
from app.crud import food as crud_food
from app.schemas.food import Food, FoodCreate, FoodUpdate
from app.db.session import engine, get_db

# Create router
router = APIRouter(
    prefix="/foods",
    tags=["Foods"]
)

@router.post("/", response_model=Food)
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    return crud_food.create_food(db, food)

@router.get("/", response_model=List[Food])
def read_foods(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    foods = crud_food.get_foods(db, skip, limit)
    return foods

@router.get("/{food_id}", response_model=Food)
def read_food(food_id: int, db: Session = Depends(get_db)):
    db_food = crud_food.get_food(db, food_id=food_id)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return db_food

@router.put("/{food_id}", response_model=Food)
def update_food(food_id: int, food: FoodUpdate, db: Session=Depends(get_db)):
    db_food = crud_food.update_food(db, food_id, food)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return db_food

@router.delete("/{food_id}", response_model=Food)
def delete_food(food_id: int, db: Session=Depends(get_db)):
    db_food = crud_food.delete_food(db, food_id)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return db_food