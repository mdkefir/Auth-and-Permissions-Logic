from django.contrib import admin

from application.models import Student, Group, Speciality, Subject, Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic', 'service_number']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic', 'record_number', 'group']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'group_number', 'form_of_education', 'speciality']

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'teacher']
