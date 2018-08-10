from django.conf.urls import include, url
from . import views
urlpatterns = [
   #url for Banner setting
    url(r'^librarybanner/$', views.librarybanner, name='librarybanner'),
]

