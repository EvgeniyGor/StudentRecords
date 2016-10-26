# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import EmbeddedModelField


class TermProject(models.Model):
    student = models.ForeignKey(UserProfile)
    projects = models.ListField(EmbeddedModelField(Project))


class Project(models.Model):
    lesson_name = models.CharField(max_length=30)
    project_title = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
