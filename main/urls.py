from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('videos/', views.videos, name='main-videos'),
    path('services/', views.services, name='main-services'),
    path('blog/', views.blog, name='main-blog'),
    path('contact/', views.contact, name='main-contact'),
]