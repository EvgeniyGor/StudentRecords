# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.attendance import Attendance
from ..models.user_profile import UserProfile


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
