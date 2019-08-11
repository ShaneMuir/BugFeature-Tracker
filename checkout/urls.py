from django.conf.urls import url
from .views import checkout_upvote

urlpatterns = [
    url(r'^upvote/$', checkout_upvote, name='checkout_upvote'),
]