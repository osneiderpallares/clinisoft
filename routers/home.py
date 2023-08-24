from fastapi import APIRouter, Request, Form, FastAPI, Path, Depends, Header
from fastapi.responses import Response
from fastapi import HTTPException, Security
from config.database import dbcreate
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests
import hashlib
from fastapi.templating import Jinja2Templates
from middlewares.jwt_bearer import JWRBearer
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from modules.varglobal import asign_value_user, userfrm
from utils.jwt_manager import create_token, validate_token
from modules.login import login
from services.login import LoginService
from modules.admisiones.pacientes import get_table_allpatients

#Verificamos si el token de autenticacion coincide con el asignados en la cookies del nav
def verify_cookies(request: Request):
    errors = []
    token = request.cookies.get("access_token")
    token=token[7:]
    if not token:
      errors.append("Authenticate first by login")
      raise HTTPException(status_code=403, detail='Credenciales son invalidas')
    else:
       data=validate_token(token)
       engine=dbcreate()
       result = LoginService().get_login(data['username'], data['password'])
       if data['username'] != result.iloc[0, 18]:
            raise HTTPException(status_code=403, detail='Credenciales son invalidas')


templates = Jinja2Templates(directory="templates/html")
home_router=APIRouter()


@home_router.get('/home/', response_class=HTMLResponse,  dependencies=[Depends(verify_cookies)])
async def def_home(request:Request):
  return templates.TemplateResponse("index.html",{"request": request})

#Verificamos si los datos de auth son correctos y asignamos el token a las cookies   
@home_router.post('/login/')
async def def_login(request:Request,response:Response, username:str = Form(...), password:str = Form(...), ):
  validation = login(username, password)
  if validation is True:
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    user = dict(username=username, password=md5_hash.hexdigest())
    token = create_token(user)
    global userfrm
    userfrm = asign_value_user(username, password)
    response = RedirectResponse(url='/home/', status_code=302)
    response.set_cookie(key="access_token", value=f'Bearer {token}', httponly=True)
    return response
  else:
      return HTMLResponse('Usuario o contraseña invalido')
  
@home_router.get('/patients/', dependencies=[Depends(verify_cookies)])
async def def_all_patients(request:Request):
  dfhtml=get_table_allpatients()
  response = templates.TemplateResponse("all-patients.html", {"request": request, "dfhtml": dfhtml})
  return response
