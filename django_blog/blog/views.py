from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog, Comment, Author
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

# Blog Views
class CreateBlogView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Blog
    fields = ["category", "title", "cover_image", "content"]
    template_name = "create_blog.html"
    success_url = reverse_lazy("blogs")

    def test_func(self):
        return self.request.user.role in ["Blogger", "Admin"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ListBlogView(ListView):
    model = Blog
    template_name = "blog_list.html"
    context_object_name = 'blogs'

class BlogView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = "blog"
    login_url = reverse_lazy('login')  

class DeleteBlogView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "delete_blog.html"
    success_url = reverse_lazy("blogs")
    
    def test_func(self):
        return self.request.user.role in ["Blogger", "Admin"]

class UpdateBlogView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ["title", "cover_image", "content", "category"]
    template_name = "update_blog.html"
    success_url = reverse_lazy("blogs")
    
    def test_func(self):
        return self.request.user.role in ["Blogger", "Admin"]

# Comments
class CreateComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = "comment_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        form.instance.blog = blog
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("blog", kwargs={"pk": self.kwargs["pk"]})

class Comments(ListView):
    model = Comment
    template_name = "comments.html"
    context_object_name = "comments"

    def get_queryset(self):
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return Comment.objects.filter(blog=blog)

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ["content"]
    template_name = "update_comment.html"

    def get_success_url(self):
        return reverse_lazy("comments", kwargs={"pk": self.object.blog.pk})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "delete_comment.html"

    def get_success_url(self):
        return reverse_lazy("comments", kwargs={"pk": self.object.blog.pk})

# Filter Posts by Tags
class PostByTagListView(ListView):
    model = Blog
    template_name = "blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs['tag_slug'])
