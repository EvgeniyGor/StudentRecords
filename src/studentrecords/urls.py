from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^(index.html)?$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^registration', include('apps.usermanager.urls', namespace='usermanager')),
    url('^datamanagement', include('apps.datamanager.urls', namespace='datamanager')),
    url('^rating', include('apps.ratingmanager.urls', namespace='ratingmanager')),
    url('^report', include('apps.reportmanager.urls', namespace='reportmanager')),
    url('^template', include('apps.templatemanager.urls', namespace='templatemanager')),
    url(r'^admin/', admin.site.urls)
]
