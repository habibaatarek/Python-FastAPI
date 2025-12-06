from fastapi import APIRouter, Depends
from blog import schema, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db= database.get_db


# create a user                       
@router.post('/', response_model=schema.ShowUser)
def create_user(request: schema.User, db : Session = Depends(get_db)):
    return user.create(request,db)

# get user by id
@router.get('/{id}', response_model=schema.ShowUser)
def get_user(id:int, db : Session = Depends(get_db)):
    return user.show(id, db)