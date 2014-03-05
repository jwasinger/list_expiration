
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login_success', 'list_app.views.login_success')
)
