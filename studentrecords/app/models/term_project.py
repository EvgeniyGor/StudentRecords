# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class Project(models.Model):
    lesson_name = models.CharField(max_length=30)
    project_title = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)


class TermProject(models.Model):
    student = models.ForeignKey(UserProfile)
    projects = ListField(EmbeddedModelField(Project))

    class Meta:
        db_table = 'termprojects'