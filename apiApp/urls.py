import imp
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MenuList, MenuDetail

urlpatterns = [
  path('menu/', MenuList.as_view()),
  path('menu/<int:pk>/', MenuDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)