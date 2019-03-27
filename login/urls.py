from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.signin, name='signin'),
   
    url(r'^face/',views.face,name='face'),
    url(r'^ghi/',views.ghi,name='ghi'),
    url(r'^tt/',views.tt,name='tt'),

] 

