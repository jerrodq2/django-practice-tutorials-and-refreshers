from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name = 'index'),
    url(r'^register', views.register, name = 'register'),
    url(r'^create', views.create, name = 'create'),
    url(r'^test_page', views.test_page, name = 'test_page'),


    url(r'^login_page', views.login_page, name = 'login_page'),
    url(r'^user_login', views.user_login, name = 'user_login'),
    url(r'^user_logout', views.user_logout, name = 'user_logout'),
]
