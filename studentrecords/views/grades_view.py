# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.grades import Grades


@login_required
def grades(request):
    grades_info = Grades.objects.all()

    return render(request, 'grades.html', {'grades': grades_info})
