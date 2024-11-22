from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from .models import Student
from app.serializers import GroupSerializer
from app.serializers import StudentSerializer


class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})

class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.all()  # Получаем все записи из модели Student
        serializer = GroupSerializer(groups, many=True)  # Сериализуем данные
        return Response(serializer.data)  # Возвращаем данные в формате JSON

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()  # Получаем все записи из модели Student
        serializer = StudentSerializer(students, many=True)  # Сериализуем данные
        return Response(serializer.data)  # Возвращаем данные в формате JSON
