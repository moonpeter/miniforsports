from django.shortcuts import render


def detail(request):
    XXX = XXX.objects.all()
    context = {:}
    return render(request, 'crawling/crawling.html', context)
