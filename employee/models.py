from django.db import models

from department.models import Department
from profession.models import Profession


class GenderChoices(models.TextChoices):
    MALE = ("male", "Male")
    FEMALE = ("female", "Female")





class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50,choices=GenderChoices.choices)
    profession = models.ForeignKey(Profession,related_name="employee_profession",on_delete=models.CASCADE)
    department = models.ForeignKey(Department,related_name="employee_department",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Employees"
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name}"
