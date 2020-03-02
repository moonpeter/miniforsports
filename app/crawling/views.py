from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView

from .models import CrawlingData


class DetailView(TemplateView):
    template_name = 'crawling/crawling.html'

# def detail(request):
#     crawlings = CrawlingData.objects.all()
#     context = {
#         'crawlingdata': CrawlingData,
#     }
#     return render(request, 'crawling/crawling.html', context)
