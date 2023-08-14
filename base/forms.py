from django import forms
from django.forms import ModelForm
from .models import User, Habit
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username',
                  'email', 'password1', 'password2', 'avatar']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avatar']


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'periodicity', 'duration']
        labels = {
            'name': 'Habit Name',
            'periodicity': 'Periodicity',
            'duration': 'Duration'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'periodicity': forms.RadioSelect(),
            'duration': forms.TextInput(attrs={'class': 'form-control'})
        }
