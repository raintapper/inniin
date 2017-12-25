from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import DetailView, View, CreateView
# Create your views here.
from profiles.models import Item
from properties.models import PropertyItem

from .forms import RegisterForm
from .models import Member

User = get_user_model()

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect("/login")
		return super(RegisterView, self).dispatch(*args, **kwargs)

class MemberFollowToggle(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		username_to_toggle = request.POST.get("username")
		member_, is_following = Member.objects.toggle_follow(request.user, username_to_toggle)
		return redirect(f"/u/{member_.user.username}/")

class MemberDetailView(DetailView):
	template_name = 'members/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context = super(MemberDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		user = context['user']
		is_following = False
		if user.member in self.request.user.is_following.all():
			is_following = True
		context['is_following'] = is_following
		query = self.request.GET.get('q')
		item_exists = Item.objects.filter(user=user).exists()
		qs = PropertyItem.objects.filter(owner=user).search(query)

		if item_exists and qs.exists():
			context['locations'] = qs
		return context