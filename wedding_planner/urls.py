"""wedding_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from apps.guest_list import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list/', include('apps.guest_list.urls')),
]

urlpatterns += [
    url(r'^wedding/create/$', views.WeddingCreate.as_view(), name='wedding_create'),
    url(r'^wedding/(?P<pk>\d+)/update/$', views.WeddingUpdate.as_view(), name='wedding_update'),
    url(r'^wedding/(?P<pk>\d+)/delete/$', views.WeddingDelete.as_view(), name='wedding_delete'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
