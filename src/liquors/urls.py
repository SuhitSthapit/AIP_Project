from django.conf.urls import url

from .views import (
	LiquorListView,
	LiquorDetailView,
	LiquorCreateView,   #, liquor_createview
	LiquorUpdateView
)

urlpatterns = [
	url(r'^create/$', LiquorCreateView.as_view(), name ='create'),  ### add liquor by a form 
	#url(r'^(?P<slug>[\w-]+)/update/$', LiquorUpdateView.as_view(), name ='update'), 	 
    url(r'^(?P<slug>[\w-]+)/$', LiquorUpdateView.as_view(), name ='detail'), ##can update and see details at same time
    url(r'^$', LiquorListView.as_view(), name ='list'),   ##list the liquors
]
