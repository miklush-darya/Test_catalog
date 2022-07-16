from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


menu = [{'title': 'О сайте', 'url_name': 'about' },
        {'title': 'Каталог', 'url_name': 'catalog'},
        {'title': 'Войти', 'url_name': 'login'}
        ]

def index(request):
    product = Catalog.objects.all()
    categs = Category.objects.all()
    context = {'product': product,
                'categs': categs,
                'menu': menu, 
                'title': 'Главная',
                'categ_selected': 0,
            }
    return render(request, 'catalog/index.html', context=context)


def about(request):
    return HttpResponse('О нас')


def catalog(request):
    product = Catalog.objects.all()
    categs = Category.objects.all()
    context = {'product': product,
                'categs': categs,
                'menu': menu, 
                'title': 'Главная',
                'categ_selected': 0,
            }
    return render(request, 'catalog/index.html', context=context)


def login(request):
    return HttpResponse('Авторизация')

def product(request):
    return HttpResponse('product')

# def categories(request, categorid):
#     print(request.GET)
#     return HttpResponse(f"<h1>Продукты по категориям</h1><p>{categorid}</p>")

def show_category (request, categ_id):
    product = Catalog.objects.filter(categ_id=categ_id)
    categs = Category.objects.all()

    if len(product) == 0:
        raise Http404()

    context = {'product': product,
                'categs': categs,
                'menu': menu, 
                'title': 'Категории',
                'categ_selected': categ_id,
            }
    return render(request, 'catalog/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")