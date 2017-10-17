from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.http import Http404
from liquors.models import LiquorList
# Create your views here.

User = get_user_model()

class ProfileDetailView(DetailView):
	template_name = 'profiles/user.html'

	def get_object(self):

		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact= username, is_active=True)

	def get_context_data (self, *args, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		user = context['user']
		query = self.request.GET.get('q')  #### text searched in SEARCH button by user
		qs = LiquorList.objects.filter (owner = user).search(query)
		#if query:
			#qs = qs.search(query)  ##query for specific user
			#qs = LiquorList.objects.search(query) #### for all the users 
		if qs.exists():
			context['liquor'] = qs
		return context
