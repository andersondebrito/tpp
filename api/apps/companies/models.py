from django.db import models
from django.db.models import SlugField, CharField


class Company(models.Model):
    slug = SlugField()
    name = CharField(max_length=50)
