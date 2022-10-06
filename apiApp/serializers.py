from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = ('id', 'menuName', 'update_at')