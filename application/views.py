from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group, Student, Teacher
from app.serializers import GroupSerializer, StudentSerializer, TeacherSerializer


class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})


class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
