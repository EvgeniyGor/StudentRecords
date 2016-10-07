from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^(index.html)?$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^registration', include('backend.usermanager.urls', namespace='usermanager')),
    url(r'^data/', include('backend.datamanager.urls', namespace='datamanager')),
    url(r'^admin/', admin.site.urls)
]
