from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, schema, models, utils, oauth
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags = ['authentication'])


@router.post('/login', response_model= schema.Token)
def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, 
        detail= f'invalid credential')
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, 
        detail= f'invalid credential')

    access_token = oauth.create_access_token(data = {'user_id': user.id})
    

    return {"access_token": access_token, 'token_type': 'bearer'}
