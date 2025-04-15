from sqlalchemy.orm import Session
import models as models
import schemas as schemas
import bcrypt

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Create a new code file
def create_codefile(db: Session, codefile: schemas.CodeFileCreate):
    db_code = models.CodeFile(**codefile.dict())
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code

# Retrieve a code file
def get_codefile(db: Session, code_id: int):
    return db.query(models.CodeFile).filter(models.CodeFile.id == code_id).first()
