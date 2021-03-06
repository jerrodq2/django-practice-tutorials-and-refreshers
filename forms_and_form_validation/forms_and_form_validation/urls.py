"""forms_and_form_validation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    url(r'^second/', include(('second_app.urls', 'second_app'), namespace='second')),
    url(r'^third/', include(('third_app.urls', 'third_app'), namespace='third')),
    url(r'^fourth/', include(('fourth_app.urls', 'fourth_app'), namespace='fourth')),
    url(r'^admin/', admin.site.urls),
]
