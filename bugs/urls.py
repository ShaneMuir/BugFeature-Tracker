from django.conf.urls import url, include
from .views import show_all_bugs, single_bug_view

urlpatterns = [
    url(r'^$', show_all_bugs, name="show_all_bugs"),
    url(r'^(?P<pk>\d+)/$', single_bug_view, name="single_bug_view")
    ]