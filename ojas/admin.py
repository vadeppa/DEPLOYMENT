from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ['id','Query','Ans']