from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, Author
from .forms import SignUpForm, LoginForm, CommentForm
from django.contrib.auth.decorators import login_required

# Registration View
class RegistrationView(CreateView):
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy('home')

# Home View
class HomeView(TemplateView):
    template_name = 'home.html'

# Login and Logout Views
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")
    
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.next_page)

# Profile View
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    login_url = reverse_lazy("login")

# Post Views
class CreatePostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ["category", "title", "cover_image", "content"]
    template_name = "create_Post.html"
    success_url = reverse_lazy("Posts")

    def test_func(self):
        return self.request.user.role in ["Postger", "Admin"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ListPostView(ListView):
    model = Post
    template_name = "Post_list.html"
    context_object_name = 'Posts'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            if Author.objects.filter(username = query):
                blogger = Author.objects.get(username = query)
                return Post.objects.filter(Blogger=blogger)

            else:
                return Post.objects.filter(title__icontains=query) | Post.objects.filter(Time__icontains = query) | Post.objects.filter(content__icontains=query) | Post.objects.filter(tags__name__icontains = query)
        return Post.objects.all()
        return super().get_queryset()

class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "Post_detail.html"
    context_object_name = "Post"
    login_url = reverse_lazy('login')  

class DeletePostView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "delete_Post.html"
    success_url = reverse_lazy("Posts")
    
    def test_func(self):
        return self.request.user.role in ["Postger", "Admin"]

class UpdatePostView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "cover_image", "content", "category"]
    template_name = "update_Post.html"
    success_url = reverse_lazy("Posts")
    
    def test_func(self):
        return self.request.user.role in ["Postger", "Admin"]

# Comments
class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = "comment_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        Post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.Post = Post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("Post", kwargs={"pk": self.kwargs["pk"]})

class Comments(ListView):
    model = Comment
    template_name = "comments.html"
    context_object_name = "comments"

    def get_queryset(self):
        Post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return Comment.objects.filter(Post=Post)

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ["content"]
    template_name = "update_comment.html"

    def get_success_url(self):
        return reverse_lazy("comments", kwargs={"pk": self.object.Post.pk})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "delete_comment.html"

    def get_success_url(self):
        return reverse_lazy("comments", kwargs={"pk": self.object.Post.pk})

# Filter Posts by Tags
class PostByTagListView(ListView):
    model = Post
    template_name = "Post_list.html"
    context_object_name = "Posts"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag_slug'])
