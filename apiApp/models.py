from turtle import update
from django.db import models

class menu(models.Model):
  menuName = models.TextField()
  update_at = models.DateTimeField(auto_now=True)
