from turtle import update
from django.db import models

class Menu(models.Model):
  menuName = models.TextField()
  update_at = models.DateTimeField(auto_now=True)
