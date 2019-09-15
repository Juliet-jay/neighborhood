from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^home/(?P<neighbourhood_id>[0-9]+)$', views.home,name= 'home'),
    url(r'^photo/(\d+)', views.single_photo, name='single_photo'),
    url(r'^search_results/',views.search_results,name='search_results'),
    
]
