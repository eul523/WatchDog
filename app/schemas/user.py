from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(min_length=1, max_length=255)
    
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)
    
class Token(BaseModel):
    access_token: str
    token_type: str