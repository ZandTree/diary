#from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import  reverse_lazy
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
#Searchfrom django.db.models import Q
from django.db.models import Q
import operator
from functools import reduce


class PostList(LoginRequiredMixin,generic.ListView):
    model = Post
    context_object_name='posts'
    login_url = 'account:login'
    paginate_by = 4

    def get_queryset(self):
        user = self.request.user
        qs = user.posts.all()
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_user"] = self.post_user
    #     return context



class CreatePost(LoginRequiredMixin,generic.CreateView):
    login_url = 'account:login'
    fields = ['title','image','text']
    model = Post
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['create_view'] = True
        return context

class DetailPost(LoginRequiredMixin,generic.DetailView):
    model = Post

class UpdatePost(LoginRequiredMixin,generic.UpdateView):
    fields = ['title','image','text']
    model = Post
    success_url = reverse_lazy('post:list')
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['edit_view'] = True
    #     return context



class DeletePost(LoginRequiredMixin,generic.DeleteView):
    model = Post
    success_url = reverse_lazy('post:list')

class Search(LoginRequiredMixin,generic.ListView):
    login_url = 'account:login'
    model = Post
    template_name = 'post/post_list.html'
    def get_queryset(self):
        user = self.request.user
        queryset = user.posts.all()
        words = self.request.GET.get('q')
        if words:
            query_list = words.split()
            result = queryset.filter(
                    reduce(operator.or_,
                           (Q(title__icontains=word) for word in query_list)) |
                    reduce(operator.or_,
                           (Q(text__icontains=word) for word in query_list))
                )
        return result
