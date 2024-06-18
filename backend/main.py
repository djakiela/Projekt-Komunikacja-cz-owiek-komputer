from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user, recipe
from database import engine, Base
from auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(recipe.router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Online Cookbook API"}
