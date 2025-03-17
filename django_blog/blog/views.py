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


class CreateBlogView(UserPassesTestMixin,LoginRequiredMixin,CreateView):
    model = Blog
    fields = ["category","Title",'Cover_image',"Content"]
    template_name = "createblog.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.role == "Blogger" or self.request.user.role == "Admin" 
    
    def form_valid(self, form):
        form.instance.Blogger = self.request.user
        return super().form_valid(form)

class ListBlogView(ListView):
    model = Blog
    template_name = "blogs.html"
    context_object_name = 'blogs'

class BlogView(LoginRequiredMixin,DetailView):
    model=Blog
    template_name="blog.html"
    context_object_name="blog"  
    login_url = reverse_lazy('login')  

class DeleteBlogView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Blog
    template_name="blog.html"
    context_object_name="blog"
    success_url = reverse_lazy('blogs')  
    def test_func(self):
        return self.request.user.role == "Blogger" or self.request.user.role == "Admin" 
    

class UpdateblogView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Blog
    template_name="updateblog.html"   
    success_url = reverse_lazy("blogs") 
    fields = ["Title","Cover_image","Content",'category']
    context_object_name='record'

    def test_func(self):
        return self.request.user.role == "Blogger" or self.request.user.role == "Admin" 
    
    def get_success_url(self):
        return reverse_lazy("blog",kwargs = {"pk":self.kwargs["pk"]})
    
class CreateComment(CreateView):
    form_class = CommentForm
    template_name = "commentform.html" 
    # success_url = reverse_lazy("blog")   

    def form_valid(self,form):
        form.instance.user = self.request.user
        blog = get_object_or_404(Blog,pk = self.kwargs['pk'])
        form.instance.blog = blog
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("blog",kwargs = {"pk":self.kwargs["pk"]})
    
class Comments(ListView):
    model = Comment
    template_name = "comments.html"
    context_object_name = "comments"    

    def get_queryset(self):
        blog = get_object_or_404(Blog,pk=self.kwargs['pk'])
        return Comment.objects.filter(blog=blog)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['blog']
    #     blog = get_object_or_404(Blog,pk=self.kwargs['pk'])
    #     return Comment.objects.filter(blog=blog)
    
    #     return super().get_context_data(**kwargs)