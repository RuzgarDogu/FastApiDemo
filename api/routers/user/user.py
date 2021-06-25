from typing import List
from fastapi import APIRouter, Depends, status
from api import schemas, database
from sqlalchemy.orm import Session
from api.modelfunctions import user

# tags > docs kısmındaki bölümleme için
router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session=Depends(get_db)):
    return user.show(id,db)
