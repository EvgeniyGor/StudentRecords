from django.shortcuts import render


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
    # user = User.objects.create_user('test', 'test', 'test@mail.ru', 'testpassword94')
    # user.save()

    return render(request, 'registration.html', {})
