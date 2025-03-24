from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from .models import CustomUser  # Ensure you have a CustomUser model if needed
from .serializers import UserSerializer

User = get_user_model()  # Ensure compatibility with custom user models

# ✅ API View for Listing All Users
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()  # Custom user model
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users

# ✅ API View for Retrieving a Single User Profile
class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ Follow a User API
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # User must be logged in

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself"}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=200)

# ✅ Unfollow a User API
class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=200)


# Create your views here.
class RegisterUserView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy("home")
    model = User

class LoginUserView(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("home")

class UserProfileView(DetailView):
    template_name = "profile,html"
    model = User
    context_object_name = "blog"  

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


