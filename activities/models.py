from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

#Creating models
class Activity(models.Model):

    ACTIVITY_TYPES = [

        ('Running', 'Running'),

        ('Cycling', 'Cycling'),

        ('Weightlifting', 'Weightlifting'),

        # Add more activity types as needed

    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)

    duration = models.PositiveIntegerField()  # in minutes

    distance = models.FloatField()  # in km or miles

    calories_burned = models.PositiveIntegerField()

    date = models.DateField()


    def __str__(self):

        return f"{self.activity_type} by {self.user.username} on {self.date}"