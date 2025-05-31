from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, Blog

def home(request):
    random_images = Image.objects.order_by('?')[:3]
    random_blog = Blog.objects.order_by('?')[:3]
    return render(request, 'index.html', {
        'images': random_images,
        'blogs': random_blog
    })  

def about(request):
    return render(request, 'about.html')

def gallery(request):
    all_images = Image.objects.all()
    return render(request, 'gallery.html', {'images': all_images})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def contacts(request):
    return render(request, 'contacts.html')
