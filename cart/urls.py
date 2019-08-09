from django.conf.urls import url
from .views import view_cart, add_to_cart, increase_cart, decrease_cart, remove_from_cart



urlpatterns = [
    url(r'^$', view_cart, name="view_cart"),
    url(r'^add/(?P<id>\d+)/$', add_to_cart, name='add_to_cart'),
    url(r'^increase/(?P<id>\d+)/$', increase_cart, name='increase_cart'),
    url(r'^decrease/(?P<id>\d+)/$', decrease_cart, name='decrease_cart'),
    url(r'^remove/(?P<id>\d+)/$', remove_from_cart, name='remove_from_cart'),
    ]