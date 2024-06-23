from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import RecipeBase, RecipeDisplay, RecipeUpdate
from models import Recipe, Ingredient, Step, User
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

    for ingredient in request.ingredients:
        new_ingredient = Ingredient(
            name=ingredient.name,
            quantity=ingredient.quantity,
            recipe_id=new_recipe.id
        )
        db.add(new_ingredient)
    
    for step in request.steps:
        new_step = Step(
            description=step.description,
            recipe_id=new_recipe.id
        )
        db.add(new_step)

    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@router.post("/admin", response_model=RecipeDisplay)
def create_recipe_admin(
    request: RecipeBase, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    if current_user.role != 'admin':
        raise HTTPException(status_code=403, detail="Not authorized")
    
    new_recipe = Recipe(
        title=request.title,
        description=request.description,
        owner_id=current_user.id
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    for ingredient in request.ingredients:
        new_ingredient = Ingredient(
            name=ingredient.name,
            quantity=ingredient.quantity,
            recipe_id=new_recipe.id
        )
        db.add(new_ingredient)
    
    for step in request.steps:
        new_step = Step(
            description=step.description,
            recipe_id=new_recipe.id
        )
        db.add(new_step)

    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@router.put("/{id}", response_model=RecipeDisplay)
def update_recipe(
    id: int,
    request: RecipeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    recipe = db.query(Recipe).filter(Recipe.id == id, Recipe.owner_id == current_user.id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    recipe.title = request.title
    recipe.description = request.description
    db.commit()

    db.query(Ingredient).filter(Ingredient.recipe_id == id).delete()
    db.query(Step).filter(Step.recipe_id == id).delete()
    db.commit()

    for ingredient in request.ingredients:
        new_ingredient = Ingredient(
            name=ingredient.name,
            quantity=ingredient.quantity,
            recipe_id=recipe.id
        )
        db.add(new_ingredient)

    for step in request.steps:
        new_step = Step(
            description=step.description,
            recipe_id=recipe.id
        )
        db.add(new_step)

    db.commit()
    db.refresh(recipe)
    return recipe

@router.get("/{id}", response_model=RecipeDisplay)
def get_recipe(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    print(f"Fetching recipe with ID: {id}")
    recipe = db.query(Recipe).filter(Recipe.id == id).first()
    if not recipe:
        print(f"Recipe with ID: {id} not found")
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
    
    db.query(Ingredient).filter(Ingredient.recipe_id == id).delete()
    db.query(Step).filter(Step.recipe_id == id).delete()
    db.delete(recipe)
    db.commit()
