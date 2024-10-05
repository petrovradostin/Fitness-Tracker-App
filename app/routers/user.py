from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data import schemas
from services import users_service
from data import database
from data.security import verify_password, create_access_token

users_router = APIRouter(prefix='/users', tags=['Users'])


def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@users_router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = users_service.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = users_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users_service.create_user(db=db, user=user)

@users_router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = users_service.get_user_by_email(db, email=user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
