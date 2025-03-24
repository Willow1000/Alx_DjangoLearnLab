from django.urls import path,include
from .views import *


urlpatterns = [
    path("register/",RegisterUserView.as_view(),name="register"),
    path("login/",LoginUserView.as_view(),name="login"),
    path("profile/",UserProfileView.as_view(),name="profile"),
    path('follow/<int:user_id>/',follow),
    path('unfollow/<int:user_id>/',unfollow)
]
