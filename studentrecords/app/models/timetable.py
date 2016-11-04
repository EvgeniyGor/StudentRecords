# -*- coding: utf-8 -*-

from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class TimeTableRecord(models.Model):
    order_number = models.IntegerField(default=1)
    lesson_name = models.CharField(max_length=50)


class TimeTableDay(models.Model):
    day_of_week = models.IntegerField(default=1)
    is_first_week = models.BooleanField()
    records = ListField(EmbeddedModelField(TimeTableRecord))


class TimeTable(models.Model):
    group = models.CharField(max_length=30)
    timetable = ListField(EmbeddedModelField(TimeTableDay))

    class Meta:
        db_table = 'timetable'