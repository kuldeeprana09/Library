from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from . import views
urlpatterns = [
    # url for Bookapp
    url(r'^$', views.index),
   # url(r'^home/$', views.index, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^event/$', views.event, name='event'),
    url(r'^donation/$', views.donation, name='donation'),
    url(r'^login/$', login, {'template_name': 'Bookapp/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'Bookapp/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    
]
