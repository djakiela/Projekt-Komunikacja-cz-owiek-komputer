from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import RecipeBase, RecipeDisplay
from models import Recipe, Ingredient, User
from database import get_db
from typing import List
from auth import get_current_user

router = APIRouter(prefix="/recipe", tags=["recipe"])

@router.post("/", response_model=RecipeDisplay)
def create_recipe(
    request: RecipeBase, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    new_recipe = Recipe(
        title=request.title,
        description=request.description,
        owner_id=current_user.id
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
def get_recipe(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    recipe = db.query(Recipe).filter(Recipe.id == id, Recipe.owner_id == current_user.id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.get("/", response_model=List[RecipeDisplay])
def get_all_recipes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    recipes = db.query(Recipe).filter(Recipe.owner_id == current_user.id).all()
    return recipes

@router.delete("/{id}", status_code=204)
def delete_recipe(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    recipe = db.query(Recipe).filter(Recipe.id == id, Recipe.owner_id == current_user.id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    # Usuwanie składników powiązanych z przepisem
    db.query(Ingredient).filter(Ingredient.recipe_id == id).delete()
    
    # Usuwanie samego przepisu
    db.delete(recipe)
    db.commit()
