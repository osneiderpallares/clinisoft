import pandas.io.sql as psql
import pandas as pd
from services.admisiones.pacientes import PatientsService
from IPython.display import HTML, display, IFrame

def get_table_allpatients():
    df=PatientsService().get_patients_basic_data()
    dfhtml=df.to_html(classes='patients-tbl table')
    return dfhtml