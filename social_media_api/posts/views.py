from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from accounts.models import *
from .serializers import *
from notifications.models import Notification
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FollowingViews(APIView):

    def get(self,request,format=None):
        following_users = request.user.following.all()
        followingPosts = Post.objects.filter(author__in = following_users).order_by
        permission_classes = [permissions.IsAuthenticated]
        return followingPosts
Post.objects.filter(author__in=following_users).order_by

class LikePost(APIView):
    def post(self,request):
        
        pk = request.kwargs['pk']
        post = generics.get_object_or_404(Post,pk =pk )
        Like.objects.get_or_create(user = request.user,post =post )
        verb = f"{request.user} like a post by {post.author}"
        Notification.objects.create(recipient = post.author,actor=request.user,verb = verb,target = post.author)