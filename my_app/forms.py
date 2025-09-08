from django import forms
from .models import Animal, Toy, Habitat
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["name", "description"]

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ["animal", "name", "color"]

class HabitatForm(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = ["name", "animals"]

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
