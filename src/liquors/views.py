from django.http import HttpResponse
from django.shortcuts import render
# Create your views here

#function based view
def home (request):
	context = {
		"logic" : True,
		 "htmlvar" : "545"
	}
	#return HttpResponse(html)                    ## To return simple HTTP response
	return render(request, "home.html", context)       ## to respond with templates ## sending context variable
	### render responds with a template called 'base.html' as per the request from url.py

def about (request):
	context = {
		"logic" : True,
		 "htmlvar" : "545"
	}
	#return HttpResponse(html)                    ## To return simple HTTP response
	return render(request, "about.html", context)      