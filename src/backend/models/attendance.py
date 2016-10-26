# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import EmbeddedModelField


class Attendance(models.Model):
    student = models.ForeignKey(UserProfile)
    attendance_records = models.ListField(EmbeddedModelField(AttendanceRecord))


class AttendanceRecord(models.Model):
    lesson_name = models.CharField(max_length=30)
    date = models.DateTimeField()

