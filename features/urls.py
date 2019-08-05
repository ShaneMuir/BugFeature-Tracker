from django.conf.urls import url
from .views import show_all_features

urlpatterns = [
    url(r'^$', show_all_features, name="show_all_features"),
    ]