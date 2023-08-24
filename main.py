from fastapi import FastAPI, Request, Form, Depends 
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.home import home_router
from config.database import dbcreate
from middlewares.jwt_bearer import JWRBearer
templates = Jinja2Templates(directory="templates/html")

app= FastAPI()
app.title = "CliniSoft"
app.version="0.0.1"
app.include_router(home_router)
app.mount("/static/", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def def_login(request:Request):
  return templates.TemplateResponse("login.html", {"request": request})

def run():
    def_login()
    
if __name__ == '__main__':
    run()