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
from django.urls import path, include
from application.views import HelloWorldAPIView
from application.views import (
    AcademListView, AttendanceListView, CourseProjectsListView, DebtAuditListView, 
    DebtsListView, DiplomaListView, DisciplesListView, EducationPlanListView, 
    FormControlListView, GradesListView, GroupListView, HoursPerSemestListView, 
    NagruzkaListView, PractiseListView, PractiseTypeListView, RatingListView, 
    RatingTypeListView, SpecialtyListView, StudentListView, TeachersListView
)
from application.views import RegisterView, LoginView, CheckPermissionsView # Auth views
from application.views import AnalyticsView # Analytic view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', HelloWorldAPIView.as_view(), name='hello_world'),
    path('api-auth/', include('rest_framework.urls')),
    path('academ/', AcademListView.as_view(), name='academ-list'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('course-projects/', CourseProjectsListView.as_view(), name='course-projects-list'),
    path('debt-audit/', DebtAuditListView.as_view(), name='debt-audit-list'),
    path('debts/', DebtsListView.as_view(), name='debts-list'),
    path('diploma/', DiplomaListView.as_view(), name='diploma-list'),
    path('disciples/', DisciplesListView.as_view(), name='disciples-list'),
    path('education-plan/', EducationPlanListView.as_view(), name='education-plan-list'),
    path('form-control/', FormControlListView.as_view(), name='form-control-list'),
    path('grades/', GradesListView.as_view(), name='grades-list'),
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('hours-per-semest/', HoursPerSemestListView.as_view(), name='hours-per-semest-list'),
    path('nagruzka/', NagruzkaListView.as_view(), name='nagruzka-list'),
    path('practise/', PractiseListView.as_view(), name='practise-list'),
    path('practise-type/', PractiseTypeListView.as_view(), name='practise-type-list'),
    path('rating/', RatingListView.as_view(), name='rating-list'),
    path('rating-type/', RatingTypeListView.as_view(), name='rating-type-list'),
    path('specialty/', SpecialtyListView.as_view(), name='specialty-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('teachers/', TeachersListView.as_view(), name='teacher-list'),
    # Auth paths
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('check-permissions/', CheckPermissionsView.as_view(), name='check-permissions'),
    # Analytics paths
    path('analyze/', AnalyticsView.as_view(), name='analyze'),
]
