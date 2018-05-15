from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^one/', views.one, name = 'one'),
    url(r'^two/', views.two, name = 'two'),
]
