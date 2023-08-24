import psycopg2
from config.database import dbcreate
import pandas.io.sql as psql
import pandas as pd

#Select principal para top 10 pacientes
class PatientsService():
    def get_patients_basic_data(self):
        conn = dbcreate()
        with conn.connect() as connection:
            dataframe = psql.read_sql(f"SELECT id, did, CONCAT(nombre1, nombre2, apellido1, apellido2), correo_electronico, generos, ciudades_nacimiento, fecha_nacimiento, ciudades_residencia, entidades, grupos_sanguineos FROM public.pacientes limit 10", conn)
        return dataframe