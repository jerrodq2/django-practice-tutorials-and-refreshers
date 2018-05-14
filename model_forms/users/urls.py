from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^form_one/', views.form_one, name = 'form_one'),
    url(r'^form_one_result/', views.form_one_result, name = 'form_one_result'),

    url(r'^form_two/', views.form_two, name = 'form_two'),
    url(r'^form_two_result/', views.form_two_result, name = 'form_two_result'),

    url(r'^form_three/', views.form_three, name = 'form_three'),
    url(r'^form_three_result/', views.form_three_result, name = 'form_three_result'),
]
