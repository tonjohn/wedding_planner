from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^view$', views.guestlist_view, name="guestlist"),
]