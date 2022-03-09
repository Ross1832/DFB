from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home_blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'