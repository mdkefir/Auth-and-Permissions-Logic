"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application.views import HelloWorldAPIView
from application.views import GroupListView, StudentListView, TeacherListView, DiscipleListView, AttendanceListView, CourseProjectListView, DiplomaListView, EducationPlanListView, FormControlListView, GradeListView, HoursPerSemestrListView, ComplexityListView, PractiseListView, PractiseTypeListView, RatingListView, RatingTypeListView, SpecialityListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', HelloWorldAPIView.as_view(), name='hello_world'),
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('disciples/', DiscipleListView.as_view(), name='disciple-list'),
    path('attendances/', AttendanceListView.as_view(), name='attendance-list'),
    path('course-projects/', CourseProjectListView.as_view(), name='course-project-list'),
    path('diplomas/', DiplomaListView.as_view(), name='diploma-list'),
    path('education-plans/', EducationPlanListView.as_view(), name='education-plan-list'),
    path('form-controls/', FormControlListView.as_view(), name='form-control-list'),
    path('grades/', GradeListView.as_view(), name='grade-list'),
    path('hours-per-semester/', HoursPerSemestrListView.as_view(), name='hours-per-semester-list'),
    path('complexities/', ComplexityListView.as_view(), name='complexity-list'),
    path('practices/', PractiseListView.as_view(), name='practice-list'),
    path('practice-types/', PractiseTypeListView.as_view(), name='practice-type-list'),
    path('ratings/', RatingListView.as_view(), name='rating-list'),
    path('rating-types/', RatingTypeListView.as_view(), name='rating-type-list'),
    path('specialities/', SpecialityListView.as_view(), name='speciality-list'),
]
