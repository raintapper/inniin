import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import PropertyItemCreateForm
from .models import PropertyItem

class PropertyListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		return PropertyItem.objects.filter(owner=self.request.user)


class PropertyDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return PropertyItem.objects.filter(owner=self.request.user)

class PropertyCreateView(LoginRequiredMixin, CreateView):
	form_class 		= PropertyItemCreateForm
	#this login_url overrides settings/base.py 's LOGIN_URL
	login_url 		= '/login/'
	template_name 	= 'form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(PropertyCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(PropertyCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Property'
		return context

class PropertyUpdateView(LoginRequiredMixin, UpdateView):
	form_class 		= PropertyItemCreateForm
	#this login_url overrides settings/base.py 's LOGIN_URL
	login_url 		= '/login/'
	template_name 	= 'properties/detail-update.html'

	def get_context_data(self, *args, **kwargs):
		context = super(PropertyUpdateView, self).get_context_data(*args, **kwargs)
		title = self.get_object().title
		context['title'] = f'Update Location: {title}' 
		return context

	def get_queryset(self):
		return PropertyItem.objects.filter(owner=self.request.user)


	













