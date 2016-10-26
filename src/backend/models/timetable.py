# -*- coding: utf-8 -*-

from django.db import models
from djangotoolbox.fields import EmbeddedModelField


class TimeTable(models.Model):
    group = models.CharField(max_length=30)
    timetable = models.ListField(EmbeddedModelField(TimeTableDay))


class TimeTableDay(models.Model):
    day_of_week = models.IntegerField(default=1)
    is_first_week = models.BooleanField()
    records = models.ListField(EmbeddedModelField(TimeTableRecord))


class TimeTableRecord(models.Model):
    order_number = models.IntegerField(default=1)
    lesson_name = models.CharField(max_length=50)
