from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  #uvicorn main:myapp --reload

class Blog(BaseModel):
    title: str 
    body: str 
    published: bool | None = None

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog has been created with title: {blog.title}"}

@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str] = None): # sort: str | None = None
    if published:
        return {'data' : f'{limit} published blogs'}
    else:
        return {'data' : f'{limit} blogs'} 

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data' : id}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return {'data' : {'1', '2'}}