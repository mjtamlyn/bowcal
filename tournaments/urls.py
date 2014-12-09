from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.TournamentList.as_view(), name='tournament-list'),
)
