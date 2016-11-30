from django.db import models
from user_profile_manager import UserProfileManager
from manager_tools import filter_by_foreign_fields


class AttendanceManager(models.Manager):
    def filter(self, **filter_fields):
        return filter_by_foreign_fields(super(AttendanceManager, self), **filter_fields)

    def create(self, user_id, attendance_records=[]):
        user_profile_manager = UserProfileManager()

        user = user_profile_manager.get(id=user_id)

        self.create(user=user, attendance_records=attendance_records)
