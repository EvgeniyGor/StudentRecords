# -*- coding: utf-8 -*-

from django.shortcuts import render
from models.user_profile import UserProfile


def students(request):
    users = list(UserProfile.objects.all())

    return render(request, 'students.html', {'users': users})


def grades(request):
    return render(request, 'grades.html', {})


def attendance(request):
    return render(request, 'attendance.html', {})


def schedule(request):
    return render(request, 'schedule.html', {})


def group_list(request):
    return render(request, 'group-list.html', {})


def term_projects(request):
    return render(request, 'term-projects.html', {})
