"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# urlpatterns_apis = [
#     path('crawling/', include('crawling.urls.apis')),
# ]
from crawling import views
from crawling.views import DetailView
from sports.views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view, name='base_view'),
    path('crawling/', DetailView.as_view(), name='detail'),
]
