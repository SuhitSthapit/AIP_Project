from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView, View
from django.http import Http404
from liquors.models import LiquorList
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

User = get_user_model()

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url =  '/'  ###homepage

	def dispatch (self, *args, **kwargs):
		#if self.request.user.is_authenticated():
		#	return redirect("/logout")
		return super(RegisterView, self).dispatch(*args, **kwargs)

class ProfileFollowToggle(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		username_to_toggle = request.POST.get("username")
		profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
		print(is_following)
		return redirect(f"/u/{profile_.user.username}/")


class ProfileDetailView(DetailView):  #### view the selected users favorite liquors and allow search as well
	template_name = 'profiles/user.html'

	def get_object(self):

		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact= username, is_active=True)

	def get_context_data (self, *args, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		user = context['user']
		is_following = False    
		if user.profile in self.request.user.is_following.all():
			is_following = True
		context['is_following'] = is_following
		query = self.request.GET.get('q')  #### text searched in SEARCH button by user
		qs = LiquorList.objects.filter (owner = user).search(query)
		#if query:
			#qs = qs.search(query)  ##query for specific user
			#qs = LiquorList.objects.search(query) #### for all the users 
		if qs.exists():
			context['liquor'] = qs
		return context
