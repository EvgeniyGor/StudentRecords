from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^attendance', attendance, name='attendance'),
    url(r'^grades', grades, name='grades'),
    url(r'^group-list', group_list, name='group-list'),
    url(r'^schedule', schedule, name='schedule'),
    url(r'^students', students, name='students'),
    url(r'^term-projects', term_projects, name='term-projects'),
    url(r'^login', login, name='login'),
    url(r'^report', get_report, name='get-report')
]
