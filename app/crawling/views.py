from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView

from .models import CrawlingData


class DetailView(View):
    def get(self, request):
        return render(request, 'crawling/crawling.html')
