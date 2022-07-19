from django.db import models

"""
A model is the single, definitive source of information about your data
Each model maps to a database table
"""

# Quick Example
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# Simply add the app to settings.py
# run python manage.py makemigrations
# then run python manage.py migrate