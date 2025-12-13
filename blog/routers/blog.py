from fastapi import APIRouter, Depends, status, HTTPException, Response
from blog import schema, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db= database.get_db


# get all blogs
@router.get('/', response_model=List[schema.ShowBlog])
def all(db : Session = Depends(get_db), get_current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)    

# create a blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)

# delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session = Depends(get_db)):
    return blog.destroy(id, db)

# update title/body
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Blog, db : Session = Depends(get_db)):
    return blog.update(id, request, db)

# get blog by id
@router.get('/{id}', status_code=200, response_model=schema.ShowBlog)
def show(id: int, db : Session = Depends(get_db)):
    return blog.get_by_id(id, db)