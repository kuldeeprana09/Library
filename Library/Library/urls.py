"""
Definition of urls for Library.
"""

from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.contrib import admin
#import Bookapp.views
#import banners.views
    #url(r'^Library', include('Library.urls'))    
    #url(r'^Library/', include('Library.Library.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # Uncomment the next two lines to enable the admin:
    # from django.contrib import admin
    # admin.autodiscover()

urlpatterns = [
    # url for Bookapp
    # url(r'^$', Bookapp.views.index, name='index'),
    #url(r'^home/$', Bookapp.views.index, name='home'),
    #url(r'^about/$', Bookapp.views.about, name='about'),
    #url(r'^contact/$', Bookapp.views.contact, name='contact'),
    #url(r'^event/$', Bookapp.views.contact, name='event'),
    #url(r'^donation/$', Bookapp.views.contact, name='donation'),
    #url(r'^login/$', login, {'template_name': 'bookapp/login.html'}),
    url(r'^Bookapp/', include('Bookapp.urls')),
    #url for Admin Setting
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url for Banner setting
     #url(r'^banners/', include('banners.urls')),
    
]
