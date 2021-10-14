"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import app.views

urlpatterns = [
    path("lone-sum/", app.views.lone_sum, name="lonesum"),
    path("cat-dog/", app.views.cat_dog, name = "catdog"),
    path("near-hundred/",app.views.near_hundred, name= "hundred"),
    path("string-splosion/", app.views.string_splosion, name = "string"),
    path('admin/', admin.site.urls),
]
