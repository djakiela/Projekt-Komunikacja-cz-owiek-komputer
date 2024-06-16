from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay, Login
from models import User
from database import get_db
from hash import Hash
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/user", tags=["user"])


# Endpoint do tworzenia nowego użytkownika
# Dodaje nowego użytkownika do bazy danych i zwraca jego szczegóły
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Endpoint do logowania użytkownika
# Sprawdza poprawność danych logowania i zwraca komunikat o sukcesie
@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return {"message": "Login successful"}


# Endpoint do wylogowania użytkownika
# Usuwa ciasteczko sesji i zwraca komunikat o wylogowaniu
@router.post("/logout")
def logout():
    response = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie(key="access_token")
    return response


# Endpoint do pobierania użytkownika po ID
# Zwraca szczegóły użytkownika na podstawie podanego ID
@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
