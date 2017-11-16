from django.core.urlresolvers import reverse_lazy

from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from . import models


class PostListView(ListView):
    model = models.Post
    context_object_name = "posts"
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):
    model = models.Post
    template_name = "posts/post_detail.html"


class PostCreateView(CreateView):
    model = models.Post
    template_name = "posts/post_new.html"
    fields = ["title", "description"]


class PostUpdateView(UpdateView):
    model = models.Post
    template_name = "posts/post_edit.html"
    fields = ["title", "description"]


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts:list")
