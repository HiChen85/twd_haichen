from django.shortcuts import render
from django.http import HttpResponse
# reverse alias of urls
from django.urls import reverse

# Create your views here.

def index(request):
    # content = '''
    # "Rango says hey there partner!"
    # <br/> <a href='/rango/about'>About</a>.
    # '''
    # return HttpResponse(content)

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'name': 'Haichen Zhang'}
    return render(request, 'rango/about.html', context=context_dict)