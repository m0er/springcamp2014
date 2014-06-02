from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<session_id>\d+)/?', 'session.views.index'),
)
