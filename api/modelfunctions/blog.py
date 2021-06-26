from sqlalchemy.orm import Session
from api.utils import schemas
from fastapi import HTTPException, status
from api.models.blog import Blog

def get_all(db:Session, limit:int):
    if limit:
        blogs = db.query(Blog).limit(limit).all()
    else:
        blogs = db.query(Blog).all()
    return blogs

def create(request:schemas.Blog, db:Session):
    new_blog = Blog(title=request.title,body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'message':'Deleted post'}

def update(id:int, request:schemas.Blog, db:Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    blog.update({'title':request.title}, synchronize_session=False)
    db.commit()
    return {'message':'Updated successfully'}

def show(id:int, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    return blog
