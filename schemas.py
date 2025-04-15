from pydantic import BaseModel, EmailStr

# User Schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

# Code File Schemas
class CodeFileCreate(BaseModel):
    filename: str
    content: str
    language: str = "python"

class CodeFileOut(BaseModel):
    id: int
    filename: str
    content: str
    language: str

    class Config:
        orm_mode = True
