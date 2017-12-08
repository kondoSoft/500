from django.apps import AppConfig

class MxvscorrupcionConfig(AppConfig):
    name = 'mxvscorrupcion'

    def ready(self):
      import mxvscorrupcion.signals