"""unicornattractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from home import urls as home_urls
from accounts import urls as accounts_urls
from bugs import urls as bugs_urls
from features import urls as features_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from search import urls as search_urls
from home.views import handler_404, handler_500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^bugs/', include(bugs_urls)),
    url(r'^features/', include(features_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^search/', include(search_urls)),
]

handler404 = handler404
handler500 = handler500


admin.site.site_header = "Unicorn Attractor"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome"

from django.contrib.auth.models import Group
admin.site.unregister(Group)