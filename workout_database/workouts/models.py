from django.db import models

class Workout(models.Model):
    #Workout models and all important information for the excersize
    name = models.CharField(max_length = 75)
    muscle_group = models.CharField(max_length = 75)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    incline = models.DecimalField(max_digits = 6, decimal_places = 2, blank = True, null = True)
    equipment = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name




