from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class ListViewAfter(ListView):
    model = Posts
    template_name = ##'index.html' ##abys věděla tak to funguje jako app/<model>_<view>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserListView(ListView):
    model = Posts
    template_name = ##:(
    context_object_name = 'posts'
    ## můžem přidat zase ordering :)
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(username=user).order_by("-date_posted")