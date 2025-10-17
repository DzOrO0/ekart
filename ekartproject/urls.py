"""
URL configuration for ekartproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from ekartApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userRegisterView.as_view(),name="reg"),
    path('login', views.LoginView.as_view(),name="login"),
    path('home', views.HomeView.as_view(),name="home_view"),
    path('pview/<int:id>', views.productView.as_view(),name="pview"),
    path('add/<int:id>', views.AddCartView.as_view(),name="add"),
    path('logout', views.Logout.as_view(),name="logout"),
    path('cartlist', views.CartListView.as_view(),name="cartlist"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
