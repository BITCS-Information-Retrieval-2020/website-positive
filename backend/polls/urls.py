from django.conf.urls import url

from polls.views import UserViewSet

urlpatterns = [
    url(r'^', UserViewSet.as_view()),
]
