from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/', views.user_register, name='register'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^profile/', views.user_profile, name='profile'),
]
