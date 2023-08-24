import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #Manipular tabla de la bd



def dbcreate():
    db_name = 'dbsystem'
    db_user = 'clinisoft'
    db_pass = 'Cmvt.023954'
    db_host = '192.168.100.50'
    db_port = '5432'

    try:
        db_string = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        engine = create_engine(db_string)
        return engine
    except Exception as ex:
        return print(str(ex), ": Error")
