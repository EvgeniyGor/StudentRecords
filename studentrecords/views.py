# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models.user_profile import UserProfile
from models.grades import Grades
from models.attendance import Attendance
from models.term_project import TermProject
from fill_db import add_users
from pdf_generator import  render_to_pdf

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
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
def students(request):
    students_info = UserProfile.objects.filter(role='s')

    return render(request, 'students.html', {'students': students_info})


@login_required
def grades(request):
    grades_info = Grades.objects.all()

    return render(request, 'grades.html', {'grades': grades_info})


@login_required
def attendance(request):
    attendance_info = Attendance.objects.all()

    return render(request, 'attendance.html', {'attendance': attendance_info})


#@login_required
def schedule(request):
    return render(request, 'timetable.html', {})


#@login_required
def group_list(request):
    students = UserProfile.objects.filter(role='s')

    group_list = {}

    for student in students:
        group = student.study_group
        if group not in group_list:
            group_list[group] = []

        group_list[group].append(student)

    return render(request, 'group-list.html', {'grouplist': group_list})


@login_required
def term_projects(request):
    projects = TermProject.objects.all()

    project_list = {}

    for project in projects:
        group = project.user.study_group
        if group not in project_list:
            project_list[group] = []

        project_list[group].append(project)

    print(project_list['2304'][0].projects)

    return render(request, 'term-projects.html', {'projectlist': project_list})



def get_report(request):
    #add_users()
    students = UserProfile.objects.filter(role='s')
    '''
    st1 = UserProfile()
    st2 = UserProfile()
    students = [st1,st2]
    '''
    article = "List of the students. Список студентов."
    #article.encode("?")
    pdf = render_to_pdf('students-to-pdf.html', {
        'article': article,
        'students': students
    })

    if pdf:
        pdf_file = open("/home/nick1/Загрузки/mygit/StudentRecords/studentrecords/static/reports/report.pdf", 'w').write(pdf)
    #return HttpResponse('this is report')
    return render(request, 'report-download.html')
