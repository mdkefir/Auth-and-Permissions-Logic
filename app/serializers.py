from rest_framework import serializers
from application.models import Administrator, Group, Student, Teacher, Disciple, Attendance, Course_project, Diploma, Education_plan, Form_control, Grade, Hours_per_semestr, Complexity, Practise, Practise_type, Rating, Rating_type, Speciality
from django.contrib.auth import get_user_model


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = Administrator.objects.create_user(email=email, password=password, **validated_data)
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class DiscipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciple
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class CourseProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_project
        fields = '__all__'


class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = '__all__'


class EducationPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_plan
        fields = '__all__'


class FormControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form_control
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class HoursPerSemestrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours_per_semestr
        fields = '__all__'


class ComplexitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Complexity
        fields = '__all__'


class PractiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practise
        fields = '__all__'


class PractiseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practise_type
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating_type
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'
