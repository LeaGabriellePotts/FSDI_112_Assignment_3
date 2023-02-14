from django.urls import re_path
from .views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
]