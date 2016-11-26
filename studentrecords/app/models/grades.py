# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class Lab(models.Model):
    title = models.CharField(max_length=50)
    grade = models.IntegerField()

    class Meta:
        db_table = 'lab'


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    labs = ListField(EmbeddedModelField(Lab))

    class Meta:
        db_table = 'lesson'


class Grades(models.Model):
    user = models.ForeignKey(UserProfile)
    grades = ListField(EmbeddedModelField(Lesson))

    class Meta:
        db_table = 'grades'
