from django.db import models
from user_profile_manager import UserProfileManager
from manager_tools import filter_by_foreign_fields


class AttendanceManager(models.Manager):
    def filter(self, **filter_fields):
        return filter_by_foreign_fields(super(AttendanceManager, self), **filter_fields)

    def create(self, student_id, attendance_records=[]):
        user_profile_manager = UserProfileManager()

        student = user_profile_manager.objects.get(id=student_id)

        self.create(student=student, attendance_records=attendance_records)
