from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)
    title = models.CharField(db_column='Title', max_length=255)
    link = models.CharField(db_column='Link', max_length=255)

    class Meta:
        managed = False
        db_table = 'book'


class Author(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)
    author = models.CharField(db_column='Author', max_length=255, null = True)

    class Meta:
        managed = False
        db_table = 'author'


class Genre(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255) 
    clas = models.FloatField(db_column='Class', max_length=255)
    genre = models.CharField(db_column='Genre', max_length=255)

    class Meta:
        managed = False
        db_table = 'genre'

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
