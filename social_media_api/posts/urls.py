from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts",PostViewSet,basename="posts")
router.register("comments",CommentViewSet,basename="comments")

urlpatterns = [
    path("api/",include(router.urls))
]
