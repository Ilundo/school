from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)


class Group(models.Model):
    title = models.CharField(max_length=50)


class Student(models.Model):
    name=models.CharField(max_length=100)

    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Schedule(models.Model):
    time=models.TimeField()

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Grade(models.Model):

    grade_choices={
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D",
        "f": "F",
    }

    value= models.CharField(max_length=1, choices=grade_choices)

    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)