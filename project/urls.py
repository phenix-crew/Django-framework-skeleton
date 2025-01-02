
from django.contrib import admin
from django.urls import path
from application import views as application_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', application_views.index),
]
