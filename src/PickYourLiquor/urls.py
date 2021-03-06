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

from django.contrib.auth.views import LoginView, LogoutView, password_reset, password_reset_done,  password_reset_complete, password_reset_confirm

from liquors.views import (
	HomeViews, ##for wheen user is loggen in
	HomeView, AboutView, 
	LiquorListView,
	LiquorDetailView,
	LiquorCreateView, liquor_createview
)
from profiles.views import RegisterView
from githubapi.views import save_githubUser
from profiles.views import ProfileFollowToggle, activate_user_view

urlpatterns = [
	url(r'^$', HomeViews.as_view(), name ='home'),
	url(r'^about/$', AboutView.as_view(),name ='about'), #instance of a class
	#url(r'^liquors/$', liquor_Listview), #function
	url(r'^liquors/', include('liquors.urls', namespace = 'liquors')),  ###include the urls.py file of app Liquors
	url(r'^u/', include('profiles.urls', namespace = 'profile')), ## u = users
	url(r'^', include('api.urls')), # include urls of api app
	#url(r'^liquors/$', LiquorListView.as_view(), name ='liquors'), 
	url(r'^login/$', LoginView.as_view(), name = 'login'),  ## logging in
	url(r'^logout/$', LogoutView.as_view(), name = 'logout'),  ## logout 
	url(r'^register/$', RegisterView.as_view(), name = 'register'),  ## Register user
	url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
	url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'), ##follow
	url(r'^password_reset/$', password_reset, name='reset'), ##password reset
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),

	#url(r'^liquors/create/$', liquor_createview),
	#url(r'^liquors/create/$', LiquorCreateView.as_view(), name ='liquours-create'),  ### add liquor by a form  
	#url(r'^liquors/(?P<slug>\w+)/$', LiquorListView.as_view()), #listView  ##slug is used to search for types of alcohols as well
    #url(r'^liquors/(?P<slug>[\w-]+)/$', LiquorDetailView.as_view(), name ='liquor-detail'),   ### pk = primary key
    url(r'^admin/', admin.site.urls),
    url(r'^web-service/', save_githubUser, name = 'webservice'),
]
