from django.shortcuts import render
from django.http import HttpResponse
# reverse alias of urls
from django.urls import reverse

from .models import Category, Page
# Create your views here.

def index(request):
    # content = '''
    # "Rango says hey there partner!"
    # <br/> <a href='/rango/about'>About</a>.
    # '''
    # return HttpResponse(content)

    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return render(request, 'rango/index.html', context=context_dict)

    # - descending order, if remove, ascending order of the result
    category_list = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'name': 'Haichen Zhang'}
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)