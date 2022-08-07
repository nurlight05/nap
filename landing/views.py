from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Article

class HomeView(TemplateView):
    
    template_name = 'landing/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:3]
        return context