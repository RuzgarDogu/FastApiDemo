from sqlalchemy.orm import Session
from api.utils import schemas
from api.models.user import User
from fastapi import HTTPException, status
from api.utils.hashing import Hash

def create(request: schemas.User, db: Session):
    hashedPassword = Hash.bcrypt(request.password)
    new_user = User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

def show(id:int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user
