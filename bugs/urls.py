from django.conf.urls import url, include
from .views import show_all_bugs, single_bug_view, upvote_bug

urlpatterns = [
    url(r'^$', show_all_bugs, name="show_all_bugs"),
    url(r'^(?P<pk>\d+)/$', single_bug_view, name="single_bug_view"),
    url(r'upvote/(?P<bug_id>[0-9]+)/$', upvote_bug, name='upvote_bug'),
    ]