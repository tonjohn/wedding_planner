from django.shortcuts import render
from django.contrib.auth import login

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Wedding
from django.contrib.auth.models import User


def index(request):
	return render(request, 'guest_list/placeholder/index.html')


def guestlist_view(request):
	user = User.objects.get(pk=1)
	login(request, user)
	return render(request, "guest_list/guest_list_show.html")


class WeddingCreate(CreateView):
	model = Wedding
	fields = '__all__'
	# initial={'date_of_death':'12/10/2016',}


class WeddingUpdate(UpdateView):
	model = Wedding
	fields = ['first_name','last_name','date_of_birth','date_of_death']


class WeddingDelete(DeleteView):
	model = Wedding
	# success_url = reverse_lazy('authors')