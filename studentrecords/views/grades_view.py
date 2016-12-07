# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.grades import Grades
from ..models.user_profile import UserProfile


@login_required
def grades(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    grades_info = []

    if profile.type == 'a':
        grades_info = get_all_grades()

    if profile.type == 's':
        grades_info = get_grades_by_student(request.user.id)

    return render(request, 'grades.html', {'grades': grades_info})


def get_grades_by_student(student_id):
    return Grades.objects.filter(user_id=student_id)


def get_all_grades():
    return Grades.objects.all()
