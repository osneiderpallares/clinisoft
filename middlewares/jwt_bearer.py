from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, Depends
from utils.jwt_manager import validate_token, create_token
from config.database import dbcreate
from services.login import LoginService
from fastapi.security import OAuth2
import jwt
from fastapi.security import OAuth2PasswordBearer

#oauth2_scheme=create_token()

class JWRBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)

        
