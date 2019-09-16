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
    # url(r'^updateProfile/', views.create_Profile, name='createProfile'),
    url(r'^business/$', views.Business, name= 'Business'),
    url(r'^neighbourhood/',views.Neighbourhood, name='Neighbourhood'),
    url(r'^Post/', views.post, name="Post"),

    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
