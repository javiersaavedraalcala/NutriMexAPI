from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from app.models import food as models_food
from app.api.v1.routes.foods import router as api_foods

# Create tables in database
models_food.Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_foods, prefix=settings.API_V1_STR)