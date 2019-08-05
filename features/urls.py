from django.conf.urls import url
from .views import show_all_features, single_feature_view

urlpatterns = [
    url(r'^$', show_all_features, name="show_all_features"),
    url(r'^(?P<pk>\d+)/$', single_feature_view, name="single_feature_view"),
    ]