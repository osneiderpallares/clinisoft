import jwt
from fastapi.responses import Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def validate_token(token:str) -> dict:
    data: dict = jwt.decode(token, key="CliniSoft2023", algorithms=['HS256',]) 
    return data

def create_token(data:dict)->str:
    token: str = jwt.encode(payload=data, key="CliniSoft2023", algorithm="HS256")
    return token