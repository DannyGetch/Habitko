# Generated by Django 4.2.4 on 2023-08-11 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_habit_options_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
    ]
