from django.db import models
from user_profile_manager import UserProfileManager
from manager_tools import filter_by_foreign_fields


class TimeTableManager(models.Manager):
    def filter(self, **filter_fields):
        return filter_by_foreign_fields(super(TimeTableManager, self), **filter_fields)

    def create(self, user_id, timetable=[]):
        user_profile_manager = UserProfileManager()

        user = user_profile_manager.profiles.get(id=user_id)

        self.create(user=user, timetable=timetable)
