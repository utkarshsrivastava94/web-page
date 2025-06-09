from django.shortcuts import render
from django.conf import settings
from .models import Resume, Link, PhotoCategory, Photo

def home(request):
    return render(request, 'portfolio/home.html')

def work_portfolio(request):
    resume = Resume.objects.last()
    links = Link.objects.all()
    return render(request, 'portfolio/work_portfolio.html', {
        'resume': resume,
        'links': links,
        'debug': settings.DEBUG  # Pass DEBUG into the template
    })

def photography_portfolio(request):
    categories = PhotoCategory.objects.all()
    return render(request, 'portfolio/photography_portfolio.html', {'categories': categories})

def photo_gallery(request, category_id):
    category = PhotoCategory.objects.get(id=category_id)
    photos = Photo.objects.filter(category=category)
    return render(request, 'portfolio/photo_gallery.html', {
        'category': category,
        'photos': photos
    })
