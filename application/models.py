from django.db import models

# Create your models here.
class Student(models.Model):
    fio = models.TextField("ФИО") # Student's name
    record_number = models.TextField("Номер зачетки")

    # group_name = models.TextField("Группа")

    group = models.ForeignKey("Group", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
    def __str__(self) -> str:
        return self.fio

class Group(models.Model):
    name = models.TextField("Название")
    form_of_education = models.TextField("Форма обучения")

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.name