from django.db import models


class Teacher(models.Model):
    name = models.TextField(max_length=255, verbose_name="ФИО")
    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self) -> str:
        return f"{self.name}"


class Student(models.Model):
    name = models.TextField(max_length=255, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    sex = models.CharField(max_length=1, verbose_name="Пол") # F - female, M - male
    school = models.TextField(max_length=255, verbose_name="Школа")
    entery_score = models.IntegerField(verbose_name="Средний бал") # ПОЧЕМУ ОН ЦЕЛЫЙ В БД? ИЛИ ЭТО НЕ БАЛ
    
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True)
    rating = models.ForeignKey("Rating", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return f"{self.name} {self.birth_date} {self.sex} {self.school} {self.entery_score} {self.group} {self.rating}"


class Group(models.Model):
    title = models.TextField(max_length=255, verbose_name="Название группы")
    code = models.TextField(max_length=255, verbose_name="Код группы")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self) -> str:
        return f"{self.code} {self.title}"

class Disciple(models.Model):
    name = models.TextField(max_length=255, verbose_name="Название дисциплины")

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

    def __str__(self) -> str:
        return f"{self.name}"
    
#Посещаемость
class Attendance(models.Model): 
    date_time = models.DateTimeField(verbose_name="Дата и время")

    student = models.ForeignKey("Student", on_delete=models.SET_NULL, null=True)
    nagruzka = models.ForeignKey("Nagruzka", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемости"

    def __str__(self) -> str:
        return f"{self.date_time} {self.student} {self.nagruzka}"


class Course_project(models.Model):
    grade = models.IntegerField(verbose_name="Оценка")

    student = models.ForeignKey("Student", on_delete=models.SET_NULL, null=True)
    hps = models.ForeignKey("Hours_per_semestr", on_delete=models.SET_NULL, null=True) #В БД hours_per_semest

    class Meta:
        verbose_name = "Курсавая работа/проект"
        verbose_name_plural = "Курсавые работы/проекты"

    def __str__(self) -> str:
        return f"{self.grade} {self.student} {self.hps}"
    
class Diploma(models.Model): # То ли диплом, то ли оценка за дисциплину
    grade = models.IntegerField(verbose_name="Оценка")

    student = models.ForeignKey("Student", on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)
    plan = models.ForeignKey("Plan", on_delete=models.SET_NULL, null=True)  

    class Meta:
        verbose_name = "Диплом?"
        verbose_name_plural = "Дипломы?"

    def __str__(self) -> str:
        return f"{self.grade} {self.student} {self.teacher} {self.plan}"

class Education_plan(models.Model):
    code = models.TextField(max_length=255, verbose_name="Код")
    year_of_conclude = models.IntegerField(verbose_name="Год завершения")

    class Meta:
        verbose_name = "Учебный план"
        verbose_name_plural = "Учебные планы"

    def __str__(self) -> str:
        return f"{self.code} {self.year_of_conclude}"
    
class Form_control(models.Model):
    form = models.TextField(max_length=255, verbose_name="Форма")
    
    hps = models.ForeignKey("Hours_per_semestr", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Форма контроля"
        verbose_name_plural = "Формы контроля"

    def __str__(self) -> str:
        return f"{self.form} {self.hps}"
    
class Grade(models.Model):
    grade = models.IntegerField(verbose_name="Оценка")
    
    student = models.ForeignKey("Student", on_delete=models.SET_NULL, null=True)
    form_control = models.ForeignKey("Form_control", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self) -> str:
        return f"{self.grade} {self.student} {self.form_control}"
    
class Hours_per_semestr(models.Model):
    hours = models.IntegerField(verbose_name="Часы")
    semester = models.IntegerField(verbose_name="Семестр")
    
    plan = models.ForeignKey("Education_plan", on_delete=models.SET_NULL, null=True)
    disciple = models.ForeignKey("Disciple", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self) -> str:
        return f"{self.hours} {self.semester} {self.plan} {self.disciple}"
    
class Nagruzka(models.Model):
 
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True)
    form_control = models.ForeignKey("Form_control", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Нагрузка"
        verbose_name_plural = "Нагрузки"

    def __str__(self) -> str:
        return f"{self.teacher} {self.group} {self.form_control}"
    
class Practise(models.Model):

    grade = models.IntegerField(verbose_name="Оценка")
 
    student = models.ForeignKey("Student", on_delete=models.SET_NULL, null=True)
    education_plan = models.ForeignKey("Education_plan", on_delete=models.SET_NULL, null=True)
    practise_type = models.ForeignKey("Practise_type", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Практика"
        verbose_name_plural = "Практики"

    def __str__(self) -> str:
        return f"{self.grade} {self.student} {self.education_plan} {self.practise_type}"
    
class Practise_type(models.Model):

    title = models.TextField(max_length=255, verbose_name="Название типа практики")
 
    class Meta:
        verbose_name = "Тип практики"
        verbose_name_plural = "Типы практики"

    def __str__(self) -> str:
        return f"{self.title}"
    
class Rating(models.Model):

    event = models.TextField(max_length=255, verbose_name="Мероприятие")
    score = models.IntegerField(verbose_name="Баллы")

    rating_type = models.ForeignKey("Rating_type", on_delete=models.SET_NULL, null=True)
 
    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self) -> str:
        return f"{self.event} {self.score} {self.rating_type}"

class Rating_type(models.Model):

    title = models.TextField(max_length=255, verbose_name="Название")
 
    class Meta:
        verbose_name = "Тип рейтинга"
        verbose_name_plural = "Типы рейтинга"

    def __str__(self) -> str:
        return f"{self.title}"
    
class Speciality(models.Model):

    code = models.TextField(max_length=255, verbose_name="Код")
    title = models.TextField(max_length=255, verbose_name="Название")
 
    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return f"{self.title} {self.code}"
