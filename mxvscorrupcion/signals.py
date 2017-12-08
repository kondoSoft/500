from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pregunta
from django.core.mail import send_mail


@receiver(post_save, sender=Pregunta)
def update_question(sender, instance, **kwargs):
  print('SENDER',sender)
  print('INSTANCIA',instance)
  return False
 

