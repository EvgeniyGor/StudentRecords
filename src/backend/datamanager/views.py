from django.shortcuts import render


def students(request):
    return render(request, 'datamanager/students.html', {})


def grades(request):
    return render(request, 'datamanager/grades.html', {})


def attendance(request):
    return render(request, 'datamanager/attendance.html', {})


def schedule(request):
    return render(request, 'datamanager/schedule.html', {})


def group_list(request):
    return render(request, 'datamanager/group-list.html', {})


def term_projects(request):
    return render(request, 'datamanager/term-projects.html', {})
