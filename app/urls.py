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
from application.views import (
    AcademListView, AttendanceListView, CourseProjectsListView, DebtAuditListView, 
    DebtsListView, DiplomaListView, DisciplesListView, EducationPlanListView, 
    FormControlListView, GradesListView, GroupListView, HoursPerSemestListView, 
    NagruzkaListView, PractiseListView, PractiseTypeListView, RatingListView, 
    RatingTypeListView, SpecialtyListView, StudentListView, TeachersListView,
    StudentIDView, TeachersIDView, GroupIDView
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from application.views import RegisterView, LoginView, CheckPermissionsView # Auth views
from application.views import AnalyticsView # Analytic view

from rest_framework.routers import DefaultRouter

from application.api import GradesViewset, SubjectStatisticsViewSet, AcademicPerformanceViewSet, AcademicReturnsViewSet, StudentRatingViewSet, GroupListViewSet, DiscipleListViewSet

router = DefaultRouter()
router.register("statistics/marks", GradesViewset, basename="grades")
router.register("statistics/subject", SubjectStatisticsViewSet, basename="subject")
router.register("academic/performance", AcademicPerformanceViewSet, basename="performance")
router.register("academic/returns", AcademicReturnsViewSet, basename="returns")
router.register("student-rating", StudentRatingViewSet, basename="rating")
router.register("groups", GroupListViewSet, basename="apigroups")
router.register("disciples", DiscipleListViewSet, basename="apidisciples")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
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
    path('groups/<int:group_id>/', GroupIDView.as_view(), name='group-id'),
    path('hours-per-semest/', HoursPerSemestListView.as_view(), name='hours-per-semest-list'),
    path('nagruzka/', NagruzkaListView.as_view(), name='nagruzka-list'),
    path('practise/', PractiseListView.as_view(), name='practise-list'),
    path('practise-type/', PractiseTypeListView.as_view(), name='practise-type-list'),
    path('rating/', RatingListView.as_view(), name='rating-list'),
    path('rating-type/', RatingTypeListView.as_view(), name='rating-type-list'),
    path('specialty/', SpecialtyListView.as_view(), name='specialty-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:student_id>/', StudentIDView.as_view(), name='student-id'),
    path('teachers/', TeachersListView.as_view(), name='teacher-list'),
    path('teachers/<int:teacher_id>/', TeachersIDView.as_view(), name='teacher-id'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('check-permissions/', CheckPermissionsView.as_view(), name='check-permissions'),

    path('analyze/', AnalyticsView.as_view(), name='analyze'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
