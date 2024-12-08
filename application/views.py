from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Group, Student, Teacher
from .permissions import IsStaffOrSuperUser
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from app.serializers import GroupSerializer, StudentSerializer, TeacherSerializer, LoginSerializer, RegisterSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

import logging

logger = logging.getLogger(__name__)

class CheckPermissionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "permissions": list(request.user.get_all_permissions())
        })


class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})


class GroupListView(APIView):
    permission_classes = [IsStaffOrSuperUser]
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset()


class StudentListView(APIView):
    permission_classes = [IsStaffOrSuperUser]
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset()
    
    
class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsStaffOrSuperUser]

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset()

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsStaffOrSuperUser]

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Administrator created successfully!'}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                })
            return Response({"error": "Неверные данные"}, status=401)
        return Response(serializer.errors, status=400)