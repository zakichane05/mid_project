from django.conf.urls import url
from . import views
app_name = 'mid_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^doctors/$', views.doctors, name='doctors'),
    url(r'^services/$', views.services, name='services'),
    url(r'^blog/$', views.blog, name='blog'),
]