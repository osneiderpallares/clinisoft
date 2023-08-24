from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from config.database import dbcreate
import requests
import hashlib
from services.login import LoginService
from utils.jwt_manager import create_token, validate_token
from middlewares.jwt_bearer import JWRBearer

#Login crea conexion a bd y retorna si el logeo fue exitoso
def login(username:str , password:str) -> bool:
    conn = dbcreate()
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    result = LoginService().get_login(username, md5_hash.hexdigest())
    if result.empty == True:
      return False
    else:
      return True