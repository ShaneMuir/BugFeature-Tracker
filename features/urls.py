from django.conf.urls import url
from .views import show_all_features, single_feature_view, create_a_feature, delete_a_feature

urlpatterns = [
    url(r'^$', show_all_features, name="show_all_features"),
    url(r'^(?P<pk>\d+)/$', single_feature_view, name="single_feature_view"),
    url(r'^(?P<pk>\d+)/delete_feature/$', delete_a_feature, name="delete_a_feature"),
    url(r'^create_feature/$', create_a_feature, name='create_a_feature'),
    ]