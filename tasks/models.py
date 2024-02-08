from django.db import models
from categories.models import Category


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=70)
    completed = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title