from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay, Login, UserUpdate
from models import User
from database import get_db
from hash import Hash
from fastapi.responses import JSONResponse
from auth import get_current_user

router = APIRouter(prefix="/user", tags=["user"])

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

@router.post("/login", response_model=UserDisplay)
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return user

@router.post("/logout")
def logout():
    response = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie(key="access_token")
    return response

@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}", response_model=UserDisplay)
def update_user(id: int, request: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if request.username is not None:
        user.username = request.username
    if request.password is not None:
        user.password = Hash.bcrypt(request.password)
    db.commit()
    db.refresh(user)
    return user

@router.get("/me", response_model=UserDisplay)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
