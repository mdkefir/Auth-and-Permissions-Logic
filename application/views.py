from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group, Student, Teacher, Disciple, Attendance, Course_project, Diploma, Education_plan, Form_control, Grade, Hours_per_semestr, Complexity, Practise, Practise_type, Rating, Rating_type, Speciality
from app.serializers import GroupSerializer, StudentSerializer, TeacherSerializer, DiscipleSerializer, AttendanceSerializer, CourseProjectSerializer, DiplomaSerializer, EducationPlanSerializer, FormControlSerializer, GradeSerializer, HoursPerSemestrSerializer, ComplexitySerializer, PractiseSerializer, PractiseTypeSerializer, RatingSerializer, RatingTypeSerializer, SpecialitySerializer


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
    

class DiscipleListView(APIView):
    def get(self, request):
        disciples = Disciple.objects.all()
        serializer = DiscipleSerializer(disciples, many=True)
        return Response(serializer.data)
    

class AttendanceListView(APIView):
    def get(self, request):
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)
    

class CourseProjectListView(APIView):
    def get(self, request):
        course_projects = Course_project.objects.all()
        serializer = CourseProjectSerializer(course_projects, many=True)
        return Response(serializer.data)
    

class DiplomaListView(APIView):
    def get(self, request):
        diplomas = Diploma.objects.all()
        serializer = DiplomaSerializer(diplomas, many=True)
        return Response(serializer.data)
    

class EducationPlanListView(APIView):
    def get(self, request):
        education_plans = Education_plan.objects.all()
        serializer = EducationPlanSerializer(education_plans, many=True)
        return Response(serializer.data)
    

class FormControlListView(APIView):
    def get(self, request):
        form_controls = Form_control.objects.all()
        serializer = FormControlSerializer(form_controls, many=True)
        return Response(serializer.data)


class GradeListView(APIView):
    def get(self, request):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)


class HoursPerSemestrListView(APIView):
    def get(self, request):
        hours_per_semesters = Hours_per_semestr.objects.all()
        serializer = HoursPerSemestrSerializer(hours_per_semesters, many=True)
        return Response(serializer.data)


class ComplexityListView(APIView):
    def get(self, request):
        complexities = Complexity.objects.all()
        serializer = ComplexitySerializer(complexities, many=True)
        return Response(serializer.data)


class PractiseListView(APIView):
    def get(self, request):
        practises = Practise.objects.all()
        serializer = PractiseSerializer(practises, many=True)
        return Response(serializer.data)


class PractiseTypeListView(APIView):
    def get(self, request):
        practise_types = Practise_type.objects.all()
        serializer = PractiseTypeSerializer(practise_types, many=True)
        return Response(serializer.data)


class RatingListView(APIView):
    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)


class RatingTypeListView(APIView):
    def get(self, request):
        rating_types = Rating_type.objects.all()
        serializer = RatingTypeSerializer(rating_types, many=True)
        return Response(serializer.data)


class SpecialityListView(APIView):
    def get(self, request):
        specialities = Speciality.objects.all()
        serializer = SpecialitySerializer(specialities, many=True)
        return Response(serializer.data)

