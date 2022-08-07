from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Tag, Article

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        context['tags'] = Tag.objects.all()
        return context