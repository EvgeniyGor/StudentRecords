from django.conf.urls import url
from views.attendance_view import attendance
from views.grades_view import grades
from views.group_list_view import group_list
from views.timetable_view import timetable
from views.students_view import students
from views.term_projects_view import term_projects
from views.auth_view import *
from views.report_view import *

urlpatterns = [
    url(r'^attendance', attendance, name='attendance'),
    url(r'^grades', grades, name='grades'),
    url(r'^group-list', group_list, name='group-list'),
    url(r'^timetable', timetable, name='timetable'),
    url(r'^students', students, name='students'),
    url(r'^term-projects', term_projects, name='term-projects'),
    url(r'^login', user_login, name='login'),
    url(r'^logout', user_logout, name='logout'),
    url(r'^report', get_report, name='get-report')
]
