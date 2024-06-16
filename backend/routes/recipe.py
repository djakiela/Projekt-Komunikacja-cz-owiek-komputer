from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import RecipeBase, RecipeDisplay
from models import Recipe, Ingredient
from database import get_db
from typing import List

router = APIRouter(prefix="/recipe", tags=["recipe"])

@router.post("/", response_model=RecipeDisplay)
def create_recipe(request: RecipeBase, db: Session = Depends(get_db)):
    new_recipe = Recipe(
        title=request.title,
        description=request.description,
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    ingredients = []
    for ingredient in request.ingredients:
        new_ingredient = Ingredient(
            name=ingredient.name,
            quantity=ingredient.quantity,
            recipe_id=new_recipe.id
        )
        db.add(new_ingredient)
        ingredients.append(new_ingredient)

    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@router.get("/{id}", response_model=RecipeDisplay)
def get_recipe(id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.get("/", response_model=List[RecipeDisplay])
def get_all_recipes(db: Session = Depends(get_db)):
    recipes = db.query(Recipe).all()
    return recipes