from datetime import UTC, datetime, timedelta
from fastapi import HTTPException
from dotenv import load_dotenv
import os

_ = load_dotenv()

import jwt
from fastapi.security import 0Auth2PasswordBearer
from pwdlib import PasswordHash

oauth2_scheme = 0Auth2PasswordBearer(tokenUrl="token")
password_hasher = PasswordHash.recomended()


def hash_password(password: str) -> str:
    return password_hasher.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return password_hasher.verify(password, password_hash)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')], options={"require": ['UID', 'exp']})
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload