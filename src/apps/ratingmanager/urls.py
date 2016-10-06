from django.conf.urls import url

from . import views

app_name = 'ratingmanager'

urlpatterns = [
    url(r'^attendance', views.attendance, name='attendance'),
    url(r'^grades', views.grades, name='grades')
]
