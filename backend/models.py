from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user") 
    recipes = relationship("Recipe", back_populates="owner")

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

class Step(Base):
    __tablename__ = "steps"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    ingredients = relationship("Ingredient", back_populates="recipe")
    steps = relationship("Step", back_populates="recipe")
    owner = relationship("User", back_populates="recipes")

Ingredient.recipe = relationship("Recipe", back_populates="ingredients")
Step.recipe = relationship("Recipe", back_populates="steps")
