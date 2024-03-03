from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()
    max_students = models.PositiveIntegerField()
    min_students = models.PositiveIntegerField()
    start_date = models.DateTimeField()


class Lesson(models.Model):
    title = models.CharField(max_length=30)
    video_link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
