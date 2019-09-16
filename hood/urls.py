from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^home/$', views.home,name= 'home'),
    url(r'^photo/(\d+)', views.single_photo, name='single_photo'),
    url(r'^search_results/',views.search_results,name='search_results'),
    url(r'^profile/$', views.profile, name='Profile'),
    url(r'^create_profile/', views.create_profile, name='create_profile'),
    url(r'^business/$', views.business, name= 'Business'),
    url(r'^business/new/$', views.create_business, name= 'create_business'),
    url(r'^neighbourhood/',views.Neighbourhood, name='Neighbourhood'),
    url(r'^Post/', views.post, name="Post"),

    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
