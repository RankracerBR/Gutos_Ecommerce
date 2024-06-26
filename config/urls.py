"""
URL configuration for config project.

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
from django.contrib import admin
from django.urls import path, include
from acesso import urls as acesso_urls
from usuarios import urls as usuarios_urls
from produtos import urls as produtos_urls
from assinantes import urls as assinantes_urls

urlpatterns = [
    path('', include(acesso_urls)),
    path('', include(usuarios_urls)),
    path('', include(produtos_urls)),
    path('', include(assinantes_urls)),
    path('admin/', admin.site.urls)
]