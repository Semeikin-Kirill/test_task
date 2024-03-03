from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Product, Team, Lesson

@admin.register(Student, Product, Team, Lesson)
class PersonAdmin(admin.ModelAdmin):
    pass
