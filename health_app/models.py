from django.db import models

class Exercise(models.Model):
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    # Other fields...

class Diet(models.Model):
    date = models.DateField()
    calories_consumed = models.PositiveIntegerField()
    # Other fields...

class Sleep(models.Model):
    date = models.DateField()
    hours_slept = models.DecimalField(max_digits=4, decimal_places=2)
    # Other fields...

class Emotion(models.Model):
    date = models.DateField()
    emotion_type = models.CharField(max_length=20)
    # Other fields...

# Define other models as needed...
# health_app/models.py

# models.py
from django.db import models

class Diets(models.Model):
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    recommendation = models.TextField(blank=True, null=True)


from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields like age, gender, etc.
class UserHealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
