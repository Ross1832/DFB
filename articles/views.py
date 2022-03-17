from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ArticleUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
