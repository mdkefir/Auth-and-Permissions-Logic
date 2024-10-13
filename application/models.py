from django.db import models


class Teacher(models.Model):
    last_name = models.TextField(max_length=30, verbose_name="Фамилия")
    first_name = models.TextField(max_length=30, verbose_name="Имя")
    patronymic = models.TextField(max_length=30, verbose_name="Отчество")

    # NOTE Возможно не пригодится
    service_number = models.TextField(max_length=15, verbose_name="Служебный номер")

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Student(models.Model):
    last_name = models.TextField(max_length=30, verbose_name="Фамилия")
    first_name = models.TextField(max_length=30, verbose_name="Имя")
    patronymic = models.TextField(max_length=30, verbose_name="Отчество")

    record_number = models.TextField(max_length=8, verbose_name="Номер зачетки")

    group = models.ForeignKey("Group", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Group(models.Model):
    name = models.TextField(max_length=30, verbose_name="Название группы")
    group_number = models.IntegerField(verbose_name="Номер группы")
    form_of_education = models.TextField(max_length=15, verbose_name="Форма обучения")

    speciality = models.ForeignKey("Speciality", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self) -> str:
        return self.name


class Speciality(models.Model):
    code = models.TextField(max_length=30, verbose_name="Код")
    name = models.TextField(max_length=30, verbose_name="Название специальности")

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return f"{self.code} {self.name}"


class Subject(models.Model):
    code = models.TextField(max_length=30, verbose_name="Код")
    name = models.TextField(max_length=30, verbose_name="Название предмета")

    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self) -> str:
        return f"{self.code} {self.name}"


class Teacher_Subject(models.Model):
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Предмет преподавателя"
        verbose_name_plural = "Предметы преподавателей"

    def __str__(self) -> str:
        return f"{self.code} {self.name}"


class Student_Subject(models.Model):
    grade = models.IntegerField(verbose_name="Оценка")

    student = models.ForeignKey("Student", on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Оценка студента"
        verbose_name_plural = "Оценки студентов"

    def __str__(self) -> str:
        return f"{self.student} {self.subject} {self.grade}"
