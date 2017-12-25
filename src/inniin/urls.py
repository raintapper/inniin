from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView

from properties.views import (PropertyListView, PropertyDetailView, PropertyCreateView)

from profiles.views import HomeView
from members.views import MemberFollowToggle, RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^member-follow/$', MemberFollowToggle.as_view(), name='follow'),
    url(r'^u/', include('members.urls', namespace='members')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^properties/', include('properties.urls', namespace='properties')),
    url(r'^items/', include('profiles.urls', namespace='profiles')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$',  TemplateView.as_view(template_name='contact.html'), name='contact'),
]
