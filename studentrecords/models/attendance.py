# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class AttendanceRecord(models.Model):
    lesson_name = models.CharField(max_length=30)
    date = models.DateTimeField()

    class Meta:
        db_table = 'attendancerecord'


class Attendance(models.Model):
    user = models.ForeignKey(UserProfile)
    attendance_records = ListField(EmbeddedModelField(AttendanceRecord))

    class Meta:
        db_table = 'attendance'
