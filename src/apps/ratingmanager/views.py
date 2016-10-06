from django.shortcuts import render


def attendance(request):
    return render(request, 'ratingmanager/attendance.html', {})


def grades(request):
    return render(request, 'ratingmanager/grades.html', {})
