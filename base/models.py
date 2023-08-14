from django.db import models

from django.contrib.auth.models import AbstractUser


PERIODICITY_CHOICES = [
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Yearly', 'Yearly')
]


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    # bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50)
    periodicity = models.CharField(
        max_length=10,
        choices=PERIODICITY_CHOICES,
        default='Daily',
    )
    duration = models.CharField(max_length=20)
    streak = models.IntegerField(default=0)
    streak_type = models.CharField(max_length=10, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    last_completed_date = models.DateTimeField(
        auto_now_add=False, auto_now=False,  blank=True, null=True)

    class Meta:
        ordering = ['-last_completed_date', '-created_date']

    def __str__(self):
        return f'Habit: {self.name} {self.periodicity}'


class CompletedHabit(models.Model):
    name = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_date = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return f'{self.completed_date}'


class Inactivity(models.Model):
    name = models.ForeignKey(Habit, on_delete=models.CASCADE)
    first_inactive_date = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True)
    last_inactive_date = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
