from django.conf.urls import patterns, url 
from .views import *

urlpatterns = [	
	url(r'^$',login_view, name = 'vista_login'),
	url(r'^logout/$',logout_view , name = 'vista_logout'),
]	