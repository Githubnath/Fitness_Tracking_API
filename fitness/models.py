from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100, default=1)
    date = models.DateField(auto_now_add= True)
    calories_burned = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100, default=1)
    sets = models.IntegerField(default=1)
    reps = models.IntegerField(default=1)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name  
    
class FitnessData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    weight = models.IntegerField(default=1)
    date = models.DateField(auto_now_add= True) 
    
    def __str__(self):
        return f'{self.user} {self.weight} {self.date} {self.exercise}'

