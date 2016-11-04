# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponseRedirect
from models.user_profile import *


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request)

    return HttpResponseRedirect('/')


def students(request):
    students_info = list(UserProfile.objects.filter(role='s'))

    return render(request, 'students.html', {'students': students_info})


def grades(request):
    return render(request, 'grades.html', {})


def attendance(request):
    return render(request, 'attendance.html', {})


def schedule(request):
    return render(request, 'timetable.html', {})


def group_list(request):
    return render(request, 'group-list.html', {})


def term_projects(request):
    return render(request, 'term-projects.html', {})
