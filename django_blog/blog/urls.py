from django.urls import path, include
from .views import *

urlpatterns = [
    path("/profile",HomeView.as_view(),name="home"),
    path("register/",RegistrationView.as_view(),name='registration'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(next_page='login'),name='logout'),
    path("createblog",CreateBlogView.as_view(),name="createblog"),
    path('blogs/',ListBlogView.as_view(),name="blogs"),
    path("post/<int:pk>/delete/",BlogView.as_view(),name="blog"),
    path("post/<int:pk>/update/",DeleteBlogView.as_view(),name = "delete"),
    path("update/<int:pk>/",UpdateblogView.as_view(),name="update"),
    path("post/new/",CreateComment.as_view(),name="comment"),
    path("blog/<int:pk>/comments",Comments.as_view(),name="comments")
    path("comment/<int:pk>/update/",Comments.as_view(),name="comments")
    path("post/<int:pk>/comments/new/",Comments.as_view(),name="comments")
    path("comment/<int:pk>/delete/",Comments.as_view(),name="comments")
    path("tags/<slug:tag_slug>/",PostByTagListView.as_view(),name="comments")
]

from Django_Blog import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)