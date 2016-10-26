# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import EmbeddedModelField


class Grades(models.Model):
    student = models.ForeignKey(UserProfile)
    grades = models.ListField(EmbeddedModelField(Lesson))


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    labs = models.ListField(EmbeddedModelField(Lab))


class Lab(models.Model):
    title = models.CharField(max_length=50)
    grade = models.DecimalField(min_value=0.0, max_value=100.0, precision=1)
