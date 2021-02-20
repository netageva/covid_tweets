from django.urls import path, include

from . import views
from django.contrib import admin
from register import views as v
urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name='home'),
    path("", views.home, name='home'),
    path("create/", views.create, name='create'),
    path("register/", v.register, name='register'),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path("view/", views.view, name='view'),

]