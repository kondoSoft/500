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

query = 'select e.nombre,e.tot100 from mxvscorrupcion_empresa as e order by e.tot100 desc;'

print(executeQuery(query))