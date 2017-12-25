from django.conf.urls import url

from .views import (
    #property_listview, 
    #property_createview
    ItemCreateView,
    ItemDetailView, 
    ItemUpdateView,
    ItemListView,
    )

urlpatterns = [
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    #url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
	url(r'^$', ItemListView.as_view(), name='list'),
	# dollarsign '$' is end of string
]
