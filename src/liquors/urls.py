from django.conf.urls import url

from .views import (
	LiquorListView,
	LiquorDetailView,
	LiquorCreateView   #, liquor_createview
)

urlpatterns = [
	url(r'^$', LiquorListView.as_view(), name ='list'),   ##list the liquors
	url(r'^create/$', LiquorCreateView.as_view(), name ='create'),  ### add liquor by a form  
    url(r'^(?P<slug>[\w-]+)/$', LiquorDetailView.as_view(), name ='detail'),   ### pk = primary key
]
