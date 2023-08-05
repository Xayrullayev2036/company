from django.db import models

from branch.models import Branch


class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, related_name="branch_department", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
