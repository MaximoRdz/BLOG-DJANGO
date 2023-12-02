from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("about/", views.about, name="about"),
    path("articles/", include("articles.urls")), 

]


urlpatterns += staticfiles_urlpatterns()