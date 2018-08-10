from django.conf.urls import include, url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    # url for Bookapp
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^event/$', views.contact, name='event'),
    url(r'^donation/$', views.contact, name='donation'),
    url(r'^login/$', login, {'template_name': 'bookapp/login.html'}),
]
