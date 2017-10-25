from django.db import connection
from django.conf import settings
import os

settings.configure()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

def executeQuery(query):
  cursor = connection.cursor()

  query = cursor.execute(query).fetchall()
  return query

query = '''select 
  p.respuesta, 
  e.nombre 
from 
  mxvscorrupcion_empresa as e 
left join 
  mxvscorrupcion_cuestionario_preguntas as cp on cp.cuestionario_id = e.cuestionario_id 
left join 
  mxvscorrupcion_pregunta as p on p.id = cp.pregunta_id 
left join 
  mxvscorrupcion_catalogo_preguntas as catp on catp.id=p.id 
where 
  catp.id = 40
order by 
  p.respuesta desc'''

print(executeQuery(query))