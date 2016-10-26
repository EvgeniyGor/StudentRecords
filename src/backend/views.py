# -*- coding: utf-8 -*-

from django.shortcuts import render
from models.user_profile import UserProfile


def students(request):
    return render(request, 'students.html', {})


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


def register(request):
    # UserProfile.create(
    #     'login',
    #     '1234',
    #     'ololo@mail.ru',
    #     first_name='Иван',
    #     last_name='Факов',
    #     patronymic='Петрович',
    #     github_id='12345',
    #     stepic_id='235'
    # )

    return render(request, 'registration.html', {})
