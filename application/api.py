from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins
from django.db.models import Avg, Count, Min, Max, Q, IntegerField, Value, Case, When
from .models import Grades
from app.serializers import GradesSerializer
from datetime import datetime
import re
from rest_framework import status
from rest_framework.views import APIView


class GradesViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Grades.objects.select_related('student', 'student__group', 'fc')
    serializer_class = GradesSerializer

    def calculate_course(self, year_of_admission: int) -> int:
        now = datetime.now()
        current_year = now.year
        current_month = now.month

        # если до сентября — курс не меняется
        if current_month < 9:
            return current_year - year_of_admission
        else:
            return current_year - year_of_admission + 1

    def extract_year_from_group_title(self, title: str) -> int | None:
        try:
            parts = title.split('-')
            year_suffix = int(parts[1])
            if year_suffix <= 25:  # допустим до 2025 года --------------------------------------
                return 2000 + year_suffix
            else:
                return 1900 + year_suffix
        except (IndexError, ValueError):
            return None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # query params
        course_param = request.query_params.get('course')
        semester = request.query_params.get('semester')
        group = request.query_params.get('group')
        subject = request.query_params.get('subject')

        if semester:
            queryset = queryset.filter(fc__hps__semester=semester)
        if group:
            queryset = queryset.filter(student__group__title__icontains=group)
        if subject:
            queryset = queryset.filter(fc__hps__disciple__disciple_name__icontains=subject)

        # для статистики: преобразуем оценки в int
        filtered_queryset = queryset.annotate(
            grade_int=Case(
                When(grade='2', then=Value(2)),
                When(grade='3', then=Value(3)),
                When(grade='4', then=Value(4)),
                When(grade='5', then=Value(5)),
                default=Value(None),
                output_field=IntegerField()
            )
        )

        stats = filtered_queryset.aggregate(
            totalStudents=Count('student', distinct=True),
            averageGrade=Avg('grade_int'),
            countGrade2=Count('grade_int', filter=Q(grade_int=2)),
            countGrade3=Count('grade_int', filter=Q(grade_int=3)),
            countGrade4=Count('grade_int', filter=Q(grade_int=4)),
            countGrade5=Count('grade_int', filter=Q(grade_int=5)),
            minGrade=Min('grade_int'),
            maxGrade=Max('grade_int')
        )

        # фильтрация по курсу, если задан
        try:
            course_param = int(course_param) if course_param else None
        except ValueError:
            course_param = None

        seen_ids = set()
        students_data = []

        for grade in filtered_queryset.select_related('student', 'student__group'):
            student = grade.student
            group = student.group
            course = None

            if group and group.title:
                year_of_admission = self.extract_year_from_group_title(group.title)
                if year_of_admission:
                    course = self.calculate_course(year_of_admission)

            # фильтрация по курсу
            if course_param and course != course_param:
                continue

            if student.student_id not in seen_ids:
                students_data.append({
                    "id": student.student_id,
                    "name": student.name,
                    "group": group.title if group else None,
                    "course": course,
                    "grade": int(grade.grade) if grade.grade and grade.grade.isdigit() else None
                })
                seen_ids.add(student.student_id)

        return Response({
            "summary": stats,
            "students": students_data
        })
    


class SubjectStatisticsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Grades.objects.select_related('student', 'student__group', 'fc')
    
    def list(self, request, *args, **kwargs):
        course = request.query_params.get('course')
        semester = request.query_params.get('semester')
        subject_name = request.query_params.get('subject')
        groups = request.query_params.get('groups', '').split(',')
        sort_by = request.query_params.get('sortBy', 'avg_grade')  # По умолчанию сортировка по avg
        limit = int(request.query_params.get('limit', 5))  # По умолчанию топ 5

        # Фильтрация по группе
        queryset = self.queryset.filter(student__group__title__in=groups)

        # Фильтрация по курсу и семестру
        if course:
            queryset = queryset.filter(student__group__course=course)
        if semester:
            queryset = queryset.filter(fc__hps__semester=semester)
        if subject_name:
            queryset = queryset.filter(fc__hps__disciple__disciple_name__icontains=subject_name)

        # Статистика для выбранного предмета
        subject_stats = queryset.aggregate(
            min_grade=Min('grade'),
            avg_grade=Avg('grade'),
            max_grade=Max('grade')
        )

        # Распределение оценок (2, 3, 4, 5)
        grade_distribution = queryset.values('grade') \
            .annotate(count=Count('grade')) \
            .order_by('grade')

        grade_distribution_bar = {
            '2': 0, '3': 0, '4': 0, '5': 0
        }
        for grade in grade_distribution:
            grade_distribution_bar[str(grade['grade'])] = grade['count']

        # Топ предметов по выбранному критерию (avg, max, count)
        top_subjects = queryset.values('fc__hps__disciple__disciple_name') \
            .annotate(
                avg_grade=Avg('grade'),
                max_grade=Max('grade'),
                count=Count('grade'),
                # avg_attendance=Avg('student__attendance'),
                # avg_activity=Avg('student__activity')
            ).order_by('-' + sort_by)[:limit]

        # Формирование ответа
        response_data = {
            "subjectStats": {
                "minGrade": subject_stats['min_grade'],
                "avgGrade": subject_stats['avg_grade'],
                "maxGrade": subject_stats['max_grade']
            },
            "gradeDistributionBar": grade_distribution_bar,
            "bestSubjects": []
        }

        for subject in top_subjects:
            response_data["bestSubjects"].append({
                "subject": subject['fc__hps__disciple__disciple_name'],
                "avg": subject['avg_grade'],
                "max": subject['max_grade'],
                "count": subject['count'],
                "avgAttendance": subject['avg_attendance'],
                "avgActivity": subject['avg_activity']
            })

        return Response(response_data, status=status.HTTP_200_OK)
