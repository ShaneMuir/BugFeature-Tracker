from django.conf.urls import url
from .views import view_cart



urlpatterns = [
    url(r'^$', view_cart, name="view_cart")
    ]