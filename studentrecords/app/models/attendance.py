# -*- coding: utf-8 -*-

from user_profile import UserProfile
from ..managers.attendance_manager import AttendanceManager
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class AttendanceRecord(models.Model):
    lesson_name = models.CharField(max_length=30)
    date = models.DateTimeField()


class Attendance(models.Model):
    student = models.ForeignKey(UserProfile)
    attendance_records = ListField(EmbeddedModelField(AttendanceRecord))

    attendance = AttendanceManager()

    class Meta:
        db_table = 'attendance'
