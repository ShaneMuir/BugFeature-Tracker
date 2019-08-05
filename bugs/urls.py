from django.conf.urls import url
from .views import (show_all_bugs, single_bug_view, upvote_bug,
                    create_a_bug, edit_a_bug, delete_a_bug)

urlpatterns = [
    url(r'^$', show_all_bugs, name="show_all_bugs"),
    url(r'^(?P<pk>\d+)/$', single_bug_view, name="single_bug_view"),
    url(r'upvote/(?P<bug_id>[0-9]+)/$', upvote_bug, name='upvote_bug'),
    url(r'^create_bug/$', create_a_bug, name="create_a_bug"),
    url(r'^(?P<pk>\d+)/edit_bug/$', edit_a_bug, name="edit_a_bug"),
    url(r'^(?P<pk>\d+)/delete_bug/$', delete_a_bug, name="delete_a_bug"),
    ]