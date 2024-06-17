from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True

class IngredientBase(BaseModel):
    name: str
    quantity: str

class IngredientDisplay(IngredientBase):
    class Config:
        orm_mode = True

class RecipeBase(BaseModel):
    title: str
    description: str
    ingredients: List[IngredientBase]

class RecipeDisplay(RecipeBase):
    ingredients: List[IngredientDisplay]

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]
