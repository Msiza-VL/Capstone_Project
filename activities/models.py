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


    

    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)

    duration = models.PositiveIntegerField(help_text='Duration in minutes')  # in minutes

    distance = models.FloatField(null=True, blank=True, help_text='Distance in kilometres')  # in km or miles

    calories_burned = models.PositiveIntegerField()

    date = models.DateField()

    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"{self.activity_type} by {self.organiser.username} on {self.date}"

    class Meta:
        verbose_name_plural = 'Activities'