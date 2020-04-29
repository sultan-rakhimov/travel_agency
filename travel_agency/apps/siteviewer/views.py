from django.shortcuts import render
from django.http import HttpResponse
from siteviewer.models import Slide
#from .forms import ContactInfo


def home(request):
    slides = Slide.objects.all()
    context = {
        'slides': slides
    }
    return render(request, 'siteviewer/home.html', context)


def contact(request):
    return render(request, 'siteviewer/contact.html')


def about(request):
    return render(request, 'siteviewer/about.html')


def news(request):
    return render(request, 'siteviewer/news.html')


def tours(request):
    return render(request, 'siteviewer/tours.html')


def slide_detail(request):
    context = {
        'image': Slide.image
    }
    return render(request, "slide_detail.html", context)
