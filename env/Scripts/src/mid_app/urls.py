from django.conf.urls import url
from . import views
app_name = 'mid_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]