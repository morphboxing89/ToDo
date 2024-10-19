from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.database import SessionLocal
from src.auth.schemas import Token, UserCreate, UserResponse
from src.auth.utils import (authenticate_user, create_access_token, get_user, get_password_hash, get_current_user,
                            oauth2_scheme)
from src.auth.models import User

router = APIRouter(prefix="/auth", tags=["auth"])

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
)

already_exists_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Username already registered",
        headers={"WWW-Authenticate": "Bearer"},
)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    with SessionLocal() as session:
        user = authenticate_user(session, form_data.username, form_data.password)
        if not user:
            raise credentials_exception
        access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate = Depends()) -> User:
    with SessionLocal() as session:
        user_from_db = get_user(session, user.username)
        if user_from_db:
            raise already_exists_exception
        hashed_password = get_password_hash(user.password)
        new_user = User(username=user.username, password=user.password, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


@router.get("/me", response_model=UserResponse)
def get_me(token: str = Depends(oauth2_scheme)):
    with SessionLocal() as session:
        user = get_current_user(session, token)
        return user
