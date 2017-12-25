from django.conf.urls import url

from .views import MemberDetailView

urlpatterns = [
    # dollarsign '$' is end of string
    url(r'^(?P<username>[\w-]+)/$', MemberDetailView.as_view(), name='detail'),
]
