# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your  account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def attendance(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    attendance_info = []

    if profile.type == 'a':
        attendance_info = get_all_attendance()

    if profile.type == 's':
        attendance_info = get_attendance_by_student(request.user.id)

    return render(request, 'attendance.html', {'attendance': attendance_info})


def get_attendance_by_student(student_id):
    return Attendance.objects.filter(user_id=student_id)


def get_all_attendance():
    return Attendance.objects.all()


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


@login_required
def group_list(request):
    students = UserProfile.objects.filter(type='s')

    group_list = {}

    for student in students:
        group = student.study_group
        if group not in group_list:
            group_list[group] = []

        group_list[group].append(student)

    return render(request, 'group-list.html', {'grouplist': group_list})

# def get_report(request):
#     students = UserProfile.objects.filter(role='s')
#     header = "List of the students. Список студентов."
#     pdf = render_to_pdf('students-to-pdf.html', {
#         'article': header,
#         'students': students
#     })
#
#     if pdf:
#         # TODO: Добавить относительный или автогенерирующийся путь
#         pdf_file = open("/home/nick1/mygit/StudentRecords/studentrecords/static/reports/report.pdf", 'w').write(pdf)
#
#     return render(request, 'report-download.html')


@login_required
def students(request):
    students_info = UserProfile.objects.filter(type='s')

    return render(request, 'students.html', {'students': students_info})


@login_required
def term_projects(request):
    projects = TermProject.objects.all()

    project_list = {}

    for project in projects:
        group = project.user.study_group
        if group not in project_list:
            project_list[group] = []

        project_list[group].append(project)

    return render(request, 'term-projects.html', {'projectlist': project_list})


@login_required
def timetable(request):
    return render(request, 'timetable.html', {})

