# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .helpers import *


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

    if profile.type == 'a' or profile.type == 't':
        attendance_info = AttendanceHelper.get_all_attendance()

    if profile.type == 's':
        attendance_info = AttendanceHelper.get_attendance_by_student(request.user.id)

    if profile.type == 'h':
        attendance_info = AttendanceHelper.get_attendance_by_group(request.user.study_group)

    return render(request, 'attendance.html', {'attendance': attendance_info})


@login_required
def grades(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    grades_info = []

    if profile.type == 'a' or profile.type == 't':
        grades_info = GradesHelper.get_all_grades()

    if profile.type == 'h':
        grades_info = GradesHelper.get_grades_by_group(request.user.study_group)

    if profile.type == 's':
        grades_info = GradesHelper.get_grades_by_student(request.user.id)

    return render(request, 'grades.html', {'grades': grades_info})


@login_required
def group_list(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    group_list_info = []

    if profile.type == 'a' or profile.type == 't':
        group_list_info = GroupListHelper.get_all_group_lists()

    if profile.type == 'h' or profile.type == 's':
        group_list_info = GroupListHelper.get_this_group_list(request.user.study_group)

    return render(request, 'group-list.html', {'grouplist': group_list_info})

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

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    term_projects_info = []

    if profile.type == 'a' or profile.type == 't':
        term_projects_info = TermProjectsHelper.get_all_term_projects()

    if profile.type == 'h' or profile.type == 's':
        term_projects_info = TermProjectsHelper.get_group_term_projects(request.user.study_group)

    return render(request, 'term-projects.html', {'projectlist': term_projects_info})


@login_required
def timetable(request):
    return render(request, 'timetable.html', {})
