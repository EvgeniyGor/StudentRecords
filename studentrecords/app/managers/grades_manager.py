from django.db import models
from user_profile_manager import UserProfileManager
from manager_tools import filter_by_foreign_fields


class GradesManager(models.Manager):
    def filter(self, **filter_fields):
        return filter_by_foreign_fields(super(GradesManager, self), **filter_fields)

    def create(self, student_id, grades=[]):
        user_profile_manager = UserProfileManager()

        student = user_profile_manager.objects.get(id=student_id)

        self.create(student=student, grades=grades)
