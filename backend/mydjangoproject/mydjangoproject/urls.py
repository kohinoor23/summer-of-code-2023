"""
URL configuration for mydjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from firstapp import views as app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', app_view.index, name='index'),
    path('firstapp/login/', app_view.login, name='login'),
    path('firstapp/signup/', app_view.signup, name='signup'),
    path('firstapp/catalogue', app_view.catalogue, name='catalogue'),
    path('firstapp/add-product', app_view.add_product, name='add-product'),
    path('firstapp/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
