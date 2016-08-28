from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/', views.register_view, name='register'),
    url(r'^login/', views.login_view),
    url(r'^logout/', views.logout_view),
]
