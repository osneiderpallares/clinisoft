import psycopg2
from config.database import dbcreate
import pandas.io.sql as psql
import pandas as pd

#Select principal para login
class LoginService():
    def get_login(self, username, password):
        conn = dbcreate()
        with conn.connect() as connection:
            dataframe = psql.read_sql(f"SELECT * FROM usuarios WHERE (correo_electronico='{username}') AND (clave='{password}')", conn)
        return dataframe
    

