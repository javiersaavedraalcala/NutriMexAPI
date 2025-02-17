from http.client import responses

import pytest
from fastapi.testclient import TestClient

def test_create_food(client):
    food_data = {
        "name": "Manzana",
        "category": "Frutas",
        "portion_size": 100,
        "portion_unit": "g",
        "calories": 52,
        "proteins": 0.3,
        "carbohydrates": 14,
        "fats": 0.2,
        "nutritional_info": {},
        "source": "USDA"
    }

    response = client.post("/api/v1/foods/", json=food_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == food_data["name"]
    assert data["category"] == food_data["category"]
    assert "id" in data

def test_read_food(client):
    # First create a food
    food_data = {
        "name": "Plátano",
        "category": "Frutas",
        "portion_size": 100,
        "portion_unit": "g",
        "calories": 89,
        "proteins": 1.1,
        "carbohydrates": 22.8,
        "fats": 0.3,
        "nutritional_info": {},
        "source": "USDA"
    }

    create_response = client.post("/api/v1/foods/", json=food_data)
    created_food = create_response.json()

    # Later we get the food created before
    response = client.get(f"/api/v1/foods/{created_food['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == food_data["name"]

def test_read_nonexistent_food(client):
    response = client.get("/api/v1/foods/999")
    assert response.status_code == 404


def test_update_food(client):
    # Primero crear un alimento
    food_data = {
        "name": "Pera",
        "category": "Frutas",
        "portion_size": 100,
        "portion_unit": "g",
        "calories": 57,
        "proteins": 0.4,
        "carbohydrates": 15.2,
        "fats": 0.1,
        "nutritional_info": {},
        "source": "USDA"
    }

    create_response = client.post("/api/v1/foods/", json=food_data)
    created_food = create_response.json()

    # Actualizar el alimento
    update_data = {
        "name": "Pera modified",
        "calories": 58
    }

    response = client.put(
        f"/api/v1/foods/{created_food['id']}",
        json={**food_data, **update_data}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["calories"] == update_data["calories"]


def test_delete_food(client):
    # First create a food
    food_data = {
        "name": "Naranja",
        "category": "Frutas",
        "portion_size": 100,
        "portion_unit": "g",
        "calories": 47,
        "proteins": 0.9,
        "carbohydrates": 11.8,
        "fats": 0.1,
        "nutritional_info": {},
        "source": "USDA"
    }

    create_response = client.post("/api/v1/foods/", json=food_data)
    created_food = create_response.json()

    # Delete the record
    response = client.delete(f"/api/v1/foods/{created_food['id']}")
    assert response.status_code == 200

    # Verified if it was deleted correctly
    get_response = client.get(f"/api/v1/foods/{created_food['id']}")
    assert get_response.status_code == 404










