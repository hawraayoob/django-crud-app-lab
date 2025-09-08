from django.db import models
from django.contrib.auth.models import User

# Primary model
class Animal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Secondary model (one-to-many with Animal)
class Toy(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Third model (many-to-many with Animal)
class Habitat(models.Model):
    name = models.CharField(max_length=100)
    animals = models.ManyToManyField(Animal)


    def __str__(self):
        return self.name
