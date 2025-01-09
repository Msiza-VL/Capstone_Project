from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
    ]

    activity_type = models.CharField(max_length=10, choices=ACTIVITY_TYPES)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    calories_burned = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.activity_type} on {self.date}'