from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^welcome/$', views.home, name='home'),
    url(r'^login/',auth_views.LoginView.as_view(template_name='login/login.html'),name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='login/logout.html'),name='logout'),


] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)