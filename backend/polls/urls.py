from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from polls import views

from polls.views import UserViewSet

urlpatterns = [
    url(r'^', UserViewSet.as_view()),
]
