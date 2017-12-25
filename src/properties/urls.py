from django.conf.urls import url

from .views import (    
    PropertyListView,
    PropertyDetailView, 
    PropertyCreateView,
    PropertyUpdateView,)

urlpatterns = [
    # dollarsign '$' is end of string
    
    url(r'^create/$', PropertyCreateView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', PropertyUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', PropertyUpdateView.as_view(), name='detail'),
    url(r'^$', PropertyListView.as_view(), name='list'),
]
