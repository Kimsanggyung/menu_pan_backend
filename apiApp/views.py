from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .serializers import MenuSerializer
from .models import Menu
class MenuList(APIView):
  def get(self, request):
    review = Menu.objects.get()
    serializer = MenuSerializer(review, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 일정 수정 및 제거 API (데이터의 아이디를 사용해서 해당 데이터 접근)    
class MenuDetail(APIView):
  def get_object(self, pk):
    try:
      return Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    todo = self.get_object(pk)
    serializer = MenuSerializer(todo)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    todo = self.get_object(pk)
    serializer = MenuSerializer(todo, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    todo = self.get_object(pk)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
