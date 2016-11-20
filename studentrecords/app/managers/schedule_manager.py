from django.db import models
from user_profile_manager import UserProfileManager
from manager_tools import filter_by_foreign_fields


class TimeTableManager(models.Manager):
    def filter(self, **filter_fields):
        return filter_by_foreign_fields(super(TimeTableManager, self), **filter_fields)

    def create(self, student_id, timetable=[]):
        user_profile_manager = UserProfileManager()

        student = user_profile_manager.objects.get(id=student_id)

        self.create(student=student, timetable=timetable)
