from django.shortcuts import render, redirect
from django.http import HttpResponse
# reverse alias of urls
from django.urls import reverse

from .models import Category, Page
from rango.forms import CategoryForm, PageForm
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
        context_dict['slug'] = category_name_slug
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', context={'form':form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:

                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print("不合法的数据输入")
            print(form.errors)
    context_dict= {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)
