from typing import List, Optional
from pydantic import BaseModel

# Request Model
class BlogBase(BaseModel):
    title: str
    body: str

# Response Model
class Blog(BlogBase):
    class Config():
        orm_mode = True

# Request Model
class User(BaseModel):
    name: str
    email: str
    password: str

# Response Model
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

# Response Model
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
