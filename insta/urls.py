
from django.urls import path
from . import views
from .views import index

app_name = 'myapp1'
urlpatterns = [
    path('', views.index, name='index'),
    path("like-post/<int:post_id>/", views.like_post, name="like_post"),
    path("profile/", views.profile_list, name="profile"),
    path("profile/<int:user_id>/", views.profile, name="profile_id"),
    path("messages/", views.message, name="messages")
]
