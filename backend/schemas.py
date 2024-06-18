from pydantic import BaseModel
from typing import List, Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
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
    owner_id: int

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

    
