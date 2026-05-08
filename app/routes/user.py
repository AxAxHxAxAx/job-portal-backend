from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.auth.hash import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.auth.dependencies import get_current_user
from app.auth.role_checker import require_role

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    #check if user already exists
    if existing_user:
        raise HTTPException(status_code=400, detail = "Email already registered")
    
    #Hash your password
    hashed_pw = hash_password(user.password)

    #Create user
    new_user = User(
        name = user.name,
        email = user.email,
        password = hashed_pw,
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User reistered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    token = create_access_token({
        "sub": db_user.email,
        "user_id": db_user.id, 
        "name": db_user.name, 
        "role": db_user.role
        })

    return {"access_token": token, "token_type": "bearer"}

@router.get("/profile")
def get_profile(current_user: str = Depends(get_current_user)):
    return {"message": f"welcome {current_user}"}

#@router.post("/createjob")
#def create_job(user: dict = Depends(require_role("recruiter"))):
#    return {"message": f"{user['name']} created a job"}

