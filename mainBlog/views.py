from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Posts, Ebooks


class ListViewAfter(ListView):
    model = Posts
    ## template_name = ##'index.html' ##abys věděla tak to funguje jako app/<model>_<view>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserListView(ListView):
    model = Posts
    ## template_name = ##:(
    context_object_name = 'posts'
    ## můžem přidat zase ordering :)
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(username=user).order_by("-date_posted")


class DetailViewAfter(DetailView):
    model = Posts


class CreateViewAfter(CreateView, LoginRequiredMixin):
    model = Posts
    fields = ['type', 'year', 'book_name', "Author_of_book", 'email', 'contacts', 'selections', 'price', 'date_posted']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return False


class DeleteViewAfter(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return False

# Ebooky
# doplníme potom až na to koukneš
