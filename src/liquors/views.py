from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  ##renders HTML files
from django.views import View  ##class based view
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import LiquorList   ## for querying (just like in admin.py)
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin ##login for class based view
from django.contrib.auth.decorators import login_required ## to login before adding data

from .forms import LiquorCreateFrom, LiquorListCreateForm
# Create your views here

@login_required(login_url = '/login/')
def liquor_createview(request):
	#print (request.POST)
	template_name = 'liquors/form.html'

	form = LiquorListCreateForm(request.POST or None)
	errors = None
	
	if form.is_valid():                #######validating form
		if request.user.is_authenticated():
			instance = form.save  (commit = False)
			instance.owner = request.user

			instance.save()
		#obj = LiquorList.objects.create(
		#	name =form.cleaned_data.get('name'),
		#	category =form.cleaned_data.get('category'),
		#	price = form.cleaned_data.get('price'),
		#	can_or_bottle =form.cleaned_data.get('can_or_bottle')
		#	)
			return HttpResponseRedirect("/liquors/")         ##return to the list of liquors of data is added
		else:
			return HttpResponseRedirect("/login/")

	if form.errors:
		errors = form.errors
		#print(form.errors)               #######else print errors
	
	context = {"form" : form, "errors" : errors}
	return render(request, template_name, context)

class LiquorCreateView(LoginRequiredMixin , CreateView):
	form_class = LiquorListCreateForm
	login_url = '/login/'
	template_name = 'form.html'
	#success_url = "/liquors/"

	def form_valid(self, form):
		instance = form.save  (commit = False)
		instance.owner = self.request.user   ##save the owner of the data added
		return super (LiquorCreateView, self).form_valid(form)

	def get_queryset(self):
		return LiquorList.objects.filter(user=self.request.user)	

	def get_context_data (self, *args, **kwargs):
		context = super(LiquorCreateView, self).get_context_data(*args, **kwargs)
		context ['title'] = 'Add Your Favorite Liquor:'
		return context

class HomeViews(View):       ####### to display items of user following
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, "home.html", {})

        user = request.user
        
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        #print (is_following_user_ids)
        qs = LiquorList.objects.filter(owner__id__in=is_following_user_ids, public=True).order_by("-updated")[:3]
        #print (qs)
        return render(request, "liquors/home-feed.html", {'object_list': qs})

#####function based view######
#def home (request):
	#context = {
	#	"logic" : True,
	#	 "htmlvar" : "545"
	#}
	#return HttpResponse(html)                    ## To return simple HTTP response
	#return render(request, "home.html", context)       ## to respond with templates ## sending context variable
	### render responds with a template called 'base.html' as per the request from url.py
   
#def liquor_Listview(request):
#	template_name = 'liquors/liquors_list.html'
#
#	queryset = LiquorList.objects.all()    ### Returns all the rows in database
#	context = {
#	"object_list" : queryset
#	}
#	return render(request, template_name, context)

class LiquorListView (LoginRequiredMixin, ListView):
	template_name = 'liquors/liquors_list.html'	
	def get_queryset(self):
		return LiquorList.objects.filter(owner=self.request.user)
		#print (self.kwargs)
		#Slug = self.kwargs.get("slug")
		#if Slug:
		#	queryset = LiquorList.objects.filter(      ###display keywords from database
				#Q(category__iexact=Slug) | Q(category__icontains=Slug)   ###contain helps to search for data even when keyword matches some part of characters from database
				#)   
		#else:
			#queryset = LiquorList.objects.all() ###display all if there is no slug
		#return queryset

class LiquorDetailView ( LoginRequiredMixin, DetailView):
	template_name = 'liquors/liquors_detail.html'
	def get_queryset(self):
		return LiquorList.objects.filter(owner=self.request.user)
	#queryset = LiquorList.objects.all()	
	
#	def get_object(self, *args, **kwargs):                 ## this function lets you to write anything instead of pk or slug in url.py
#		liquor_id = self.kwargs.get('liquor_id')
#		obj = get_object_or_404(LiquorList, id = liquor_id)  ## pk = liquor_id
#		return obj

class LiquorUpdateView (LoginRequiredMixin, UpdateView):   ##to update details
	template_name = 'liquors/detail-update.html'
	form_class = LiquorListCreateForm
	
	def get_queryset(self):
		return LiquorList.objects.filter(owner = self.request.user)	

	def get_context_data (self, *args, **kwargs):
		context = super(LiquorUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context ['title'] = f"Update Your Favorite Liquor: {name}"
		return context


### class Template based view ###
class HomeView (TemplateView):
	template_name = "home.html"

class AboutView (TemplateView):
	template_name = "about.html"
 

