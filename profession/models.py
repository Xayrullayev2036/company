from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Profession"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
