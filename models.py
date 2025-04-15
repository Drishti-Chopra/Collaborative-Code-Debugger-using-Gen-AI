from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="collaborator")
    codes = relationship("CodeFile", back_populates="owner")

class CodeFile(Base):
    __tablename__ = "code_files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(Text)
    language = Column(String, default="python")
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="codes")
