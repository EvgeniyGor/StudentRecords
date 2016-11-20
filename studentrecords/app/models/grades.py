# -*- coding: utf-8 -*-

from user_profile import UserProfile
from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField


class Lab(models.Model):
    title = models.CharField(max_length=50)
    grade = models.DecimalField()


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    labs = ListField(EmbeddedModelField(Lab))


class Grades(models.Model):
    student = models.ForeignKey(UserProfile)
    grades = ListField(EmbeddedModelField(Lesson))

    @staticmethod
    def create(student_id, grades=[]):
        student = UserProfile.objects.get_by_login(id=student_id)
        grade = Grades.objects.create(student=student, grades=grades)
        grade.save()

        return grade

    class Meta:
        db_table = 'grades'
