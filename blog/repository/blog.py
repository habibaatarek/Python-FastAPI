from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import HTTPException, status


# get all blogs
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

# create a blog
def create(request: schema.Blog, db: Session):
    new_blog =models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# delete a blog
def destroy(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'

# update title/body
def update(id: int, request: schema.Blog, db: Session):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first ():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not found")
    blog.update(request.dict())
    db.commit()
    return 'Updated'

# get blog by id
def get_by_id(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    return blog