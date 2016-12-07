# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.user_profile import UserProfile


@login_required
def group_list(request):
    students = UserProfile.objects.filter(role='s')

    group_list = {}

    for student in students:
        group = student.study_group
        if group not in group_list:
            group_list[group] = []

        group_list[group].append(student)

    return render(request, 'group-list.html', {'grouplist': group_list})
