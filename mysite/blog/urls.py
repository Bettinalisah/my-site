from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('posts', views.posts, name="post-page"),
    path('posts/<slug:slug>', views.post_details, name="post_details")
]