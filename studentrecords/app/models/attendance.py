# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class AttendanceRecord(models.Model):
    lesson_name = models.CharField(max_length=30)
    date = models.DateTimeField()


class Attendance(models.Model):
    student = models.ForeignKey(UserProfile)
    attendance_records = ListField(EmbeddedModelField(AttendanceRecord))

    @staticmethod
    def create(student_id, attendance_records=[]):
        student = UserProfile.objects.get_by_login(id=student_id)
        attendance = Attendance.objects.create(student=student, attendance_records=attendance_records)
        attendance.save()

        return attendance

    class Meta:
        db_table = 'attendance'