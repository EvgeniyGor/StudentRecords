# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models.user_profile import UserProfile
from models.grades import Grades
from models.attendance import Attendance


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
    students_info = UserProfile.objects.filter(role='s')

    return render(request, 'students.html', {'students': students_info})


def grades(request):

    grades_info = Grades.objects.all()

    return render(request, 'grades.html', {'grades': grades_info})


def attendance(request):

    attendance_info = Attendance.objects.all()

    return render(request, 'attendance.html', { 'attendance': attendance_info})


def schedule(request):
    return render(request, 'timetable.html', {})


def group_list(request):
    return render(request, 'group-list.html', {})


def term_projects(request):
    return render(request, 'term-projects.html', {})


def get_report(request):
    return HttpResponse('this is report')