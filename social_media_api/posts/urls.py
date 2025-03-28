from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts",PostViewSet,basename="posts")
router.register("comments",CommentViewSet,basename="comments")

urlpatterns = [
    path("",include(router.urls)),
    path("feed/",FollowingViews.as_view()),
    path("/posts/<int:pk>/like/",LikePost.as_view()),
    path("/posts/<int:pk>/unlike/",UnlikePost.as_view())
]
