"""PickYourLiquor URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import LoginView

from liquors.views import (
	HomeView, AboutView, 
	LiquorListView,
	LiquorDetailView,
	LiquorCreateView, liquor_createview
)

urlpatterns = [
	url(r'^$', HomeView.as_view(), name ='home'),
	url(r'^about/$', AboutView.as_view(),name ='about'), #instance of a class
	#url(r'^liquors/$', liquor_Listview), #function
	 url(r'^liquors/', include('liquors.urls', namespace = 'liquors')),  ###include the urls.py file of app Liquors
	#url(r'^liquors/$', LiquorListView.as_view(), name ='liquors'), 
	url(r'^login/$', LoginView.as_view(), name = 'login'),  ## logging in
	#url(r'^liquors/create/$', liquor_createview),
	#url(r'^liquors/create/$', LiquorCreateView.as_view(), name ='liquours-create'),  ### add liquor by a form  
	#url(r'^liquors/(?P<slug>\w+)/$', LiquorListView.as_view()), #listView  ##slug is used to search for types of alcohols as well
    #url(r'^liquors/(?P<slug>[\w-]+)/$', LiquorDetailView.as_view(), name ='liquor-detail'),   ### pk = primary key
    url(r'^admin/', admin.site.urls),
]
