from django.conf.urls import url

from . import views

app_name = 'datamanager'

urlpatterns = [
    url(r'^attendance', views.attendance, name='attendance'),
    url(r'^grades', views.grades, name='grades'),
    url(r'^group-list', views.group_list, name='group-list'),
    url(r'^schedule', views.schedule, name='schedule'),
    url(r'^students', views.students, name='students'),
    url(r'^term-projects', views.term_projects, name='term-projects')
]
