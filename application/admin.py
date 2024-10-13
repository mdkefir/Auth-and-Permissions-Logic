from django.contrib import admin

from application.models import Student, Group

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['fio', 'record_number', 'group']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "form_of_education"]