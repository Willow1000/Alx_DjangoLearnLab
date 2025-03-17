from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView
from .forms import SignUpForm,LoginForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
# Create your views here.

class RegistrationView(CreateView):
    form_class = SignUpForm
    template_name = "register.html"
    success_url = reverse_lazy('home')

class HomeView(TemplateView):
    template_name = 'home.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    # redirect_authenticated_user = True
    next_page= reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")    
    def dispatch(self, request, *args, **kwargs):
        logout(request)  # Ensure session is cleared
        return redirect(self.next_page)


class CreatePostView(UserPassesTestMixin,LoginRequiredMixin,CreateView):
    model = Post
    fields = ["category","Title",'Cover_image',"Content"]
    template_name = "createPost.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.role == "Postger" or self.request.user.role == "Admin" 
    
    def form_valid(self, form):
        form.instance.Postger = self.request.user
        return super().form_valid(form)

class ListPostView(ListView):
    model = Post
    template_name = "Posts.html"
    context_object_name = 'Posts'

class PostView(LoginRequiredMixin,DetailView):
    model=Post
    template_name="Post.html"
    context_object_name="Post"  
    login_url = reverse_lazy('login')  

class DeletePostView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Post
    template_name="Post.html"
    context_object_name="Post"
    success_url = reverse_lazy('Posts')  
    def test_func(self):
        return self.request.user.role == "Postger" or self.request.user.role == "Admin" 
    

class UpdatePostView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Post
    template_name="updatePost.html"   
    success_url = reverse_lazy("Posts") 
    fields = ["Title","Cover_image","Content",'category']
    context_object_name='record'

    def test_func(self):
        return self.request.user.role == "Postger" or self.request.user.role == "Admin" 
    
    def get_success_url(self):
        return reverse_lazy("Post",kwargs = {"pk":self.kwargs["pk"]})
    
class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = "commentform.html" 
    # success_url = reverse_lazy("Post")   

    def form_valid(self,form):
        form.instance.user = self.request.user
        Post = get_object_or_404(Post,pk = self.kwargs['pk'])
        form.instance.Post = Post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("Post",kwargs = {"pk":self.kwargs["pk"]})
    
class Comments(ListView):
    model = Comment
    template_name = "comments.html"
    context_object_name = "comments"    

    def get_queryset(self):
        Post = get_object_or_404(Post,pk=self.kwargs['pk'])
        return Comment.objects.filter(Post=Post)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Post']
    #     Post = get_object_or_404(Post,pk=self.kwargs['pk'])
    #     return Comment.objects.filter(Post=Post)
    
    #     return super().get_context_data(**kwargs)

class CommentUpdateView(UpdateView):
    pass