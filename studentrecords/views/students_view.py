# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.user_profile import UserProfile


@login_required
def students(request):
    students_info = UserProfile.objects.filter(role='s')

    return render(request, 'students.html', {'students': students_info})

