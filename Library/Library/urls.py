"""
Definition of urls for Library.
"""

from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.contrib import admin
from Library import views 

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # Uncomment the next two lines to enable the admin:
    # from django.contrib import admin
    # admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^Bookapp/', include('Bookapp.urls')),
    #url for Admin Setting
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url for Banner setting
     #url(r'^banners/', include('banners.urls')),
    
]
