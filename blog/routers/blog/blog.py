from typing import List
from fastapi import APIRouter, Depends, status
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

get_db = database.get_db

"""
Bazı apiler için user girişi gerekli olabilir. O yüzden onlar için depends tanımlanıyor.
get_current_user:schemas.User = Depends(oauth2.get_current_user)
"""
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

"""
API'ye post etmek için aşağıdaki kullanılıyor.
ÖNEMLİ !!!!  >>> hem schemas, hem de models kullanılıyor
Sebebi de models veritabanı için, schemas ise API tarafında
client'tan verileri almak için.
Yani api'den istediğimiz şekilde alabilir. db'de ise istediğimiz gibi post edebiliriz.
"""
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session=Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session=Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

"""
response_model > göstereceğimiz model. Yani request olarak istediğimiz değil
client tarafına göndereceğimiz model.
"""
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id:int, db: Session=Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    # return db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog.show(id,db)
