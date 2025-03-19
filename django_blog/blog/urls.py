from django.urls import path, include
from .views import *

urlpatterns = [
    path("profile/", HomeView.as_view(), name="home"),
    path("register/", RegistrationView.as_view(), name="registration"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("createblog/", CreateBlogView.as_view(), name="createblog"),
    path("blogs/", ListBlogView.as_view(), name="blogs"),
    path("post/<int:pk>/delete/", DeleteBlogView.as_view(), name="delete-blog"),
    path("post/<int:pk>/update/", UpdateBlogView.as_view(), name="update-blog"),
    path("post/new/", CreateComment.as_view(), name="new-comment"),
    path("blog/<int:pk>/comments/", Comments.as_view(), name="blog-comments"),
    path("comment/<int:pk>/update/", Comments.as_view(), name="update-comment"),
    path("post/<int:pk>/comments/new/", Comments.as_view(), name="new-comment"),
    path("comment/<int:pk>/delete/", Comments.as_view(), name="delete-comment"),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),
    path("profile/", ProfileView.as_view(), name="profile"),
]

# Serving media files in development mode
from Django_Blog import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
