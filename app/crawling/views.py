from django.shortcuts import render


def detail(request):
    return render(request, 'crawling/crawling.html')
