from django.conf.urls import url, include
from .views import show_all_bugs

urlpatterns = [
    url(r'^$', show_all_bugs, name="show_all_bugs")
    ]