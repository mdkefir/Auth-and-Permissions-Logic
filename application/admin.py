from django.contrib import admin

from .models import (
    Teacher, Student, Group, Disciple, Attendance, Course_project, Diploma,
    Education_plan, Form_control, Grade, Hours_per_semestr, Nagruzka, Practise,
    Practise_type, Rating, Rating_type, Speciality
)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'sex', 'school', 'entery_score', 'group', 'rating']
    list_filter = ['sex', 'group', 'rating']
    search_fields = ['name', 'school']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['code', 'title']
    search_fields = ['code', 'title']

@admin.register(Disciple)
class DiscipleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'student', 'nagruzka']
    list_filter = ['date_time']
    search_fields = ['student__name']

@admin.register(Course_project)
class CourseProjectAdmin(admin.ModelAdmin):
    list_display = ['grade', 'student', 'hps']
    search_fields = ['student__name']

@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = ['grade', 'student', 'teacher', 'education_plan']
    search_fields = ['student__name', 'teacher__name']

@admin.register(Education_plan)
class EducationPlanAdmin(admin.ModelAdmin):
    list_display = ['code', 'year_of_conclude']
    search_fields = ['code']

@admin.register(Form_control)
class FormControlAdmin(admin.ModelAdmin):
    list_display = ['form', 'hps']
    search_fields = ['form']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['grade', 'student', 'form_control']
    search_fields = ['student__name']

@admin.register(Hours_per_semestr)
class HoursPerSemesterAdmin(admin.ModelAdmin):
    list_display = ['hours', 'semester', 'plan', 'disciple']
    search_fields = ['disciple__name', 'plan__code']

@admin.register(Nagruzka)
class NagruzkaAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'group', 'form_control']
    search_fields = ['teacher__name', 'group__title']

@admin.register(Practise)
class PractiseAdmin(admin.ModelAdmin):
    list_display = ['grade', 'student', 'education_plan', 'practise_type']
    search_fields = ['student__name', 'practise_type__title']

@admin.register(Practise_type)
class PractiseTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['event', 'score', 'rating_type']
    search_fields = ['event', 'rating_type__title']

@admin.register(Rating_type)
class RatingTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['code', 'title']
    search_fields = ['title', 'code']

