from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.services.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/register")
def register(
    phone: str,
    password: str,
    email: str = None,
    db: Session = Depends(get_db)
):
    # Check if user exists
    existing = db.query(User).filter(
        (User.phone == phone) | (User.email == email)
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=400,
            detail="User with this phone or email already exists"
        )
    
    # Create user
    user = User(
        phone=phone,
        email=email,
        password_hash=hash_password(password)
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {
        "status": "success",
        "message": "User registered successfully",
        "user_id": user.id
    }

@router.post("/login")
def login(
    phone: str,
    password: str,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.phone == phone).first()
    
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create token
    token = create_access_token({
        "sub": str(user.id),
        "phone": user.phone,
        "role": user.role
    })
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id,
        "trust_score": user.trust_score
    }
