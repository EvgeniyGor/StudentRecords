# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.attendance import Attendance


@login_required
def attendance(request):
    attendance_info = get_attendance_for_student(request.user.id)

    return render(request, 'attendance.html', {'attendance': attendance_info})


def get_attendance_for_student(student_id):
    return Attendance.objects.filter(user_id=student_id)