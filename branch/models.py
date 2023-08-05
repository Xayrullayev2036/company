from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    branch_phone = models.CharField(max_length=100)
    branch_email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branch"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
