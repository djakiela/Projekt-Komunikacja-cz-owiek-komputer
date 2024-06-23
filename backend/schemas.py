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
    role: str

    class Config:
        orm_mode = True

class IngredientBase(BaseModel):
    name: str
    quantity: str

class IngredientDisplay(IngredientBase):
    class Config:
        orm_mode = True

class StepBase(BaseModel):
    description: str

class StepDisplay(StepBase):
    class Config:
        orm_mode = True

class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    ingredients: List[IngredientBase]
    steps: List[StepBase]

class RecipeDisplay(RecipeBase):
    id: int
    ingredients: List[IngredientDisplay]
    steps: List[StepDisplay]
    owner_id: int

    class Config:
        orm_mode = True

class RecipeUpdate(BaseModel):
    title: str
    description: Optional[str]
    ingredients: List[IngredientBase]
    steps: List[StepBase]

class Login(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
