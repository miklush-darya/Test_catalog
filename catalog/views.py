from django.views.generic import ListView, CreateView
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить продукт", 'url_name': 'add_page'},
        {'title': "Войти", 'url_name': 'login'},
        # {'title': "Обратная связь", 'url_name': 'contact'},
        ]


def about(request):
    return render(request, 'catalog/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(CreateView):
    form_class=AddProdForm
    template_name = 'catalog/add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):   #*, object_list=None,
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['product'] = Catalog.objects.all()
        context['categs'] = Category.objects.all()
        # # context['categ_selected'] = 0
        return context

    # def form_valid(self, form):
    #     form.save()
    #     return redirect("home")


# def addpr(request):
#     if request.method == 'POST':
#         form = AddProdForm(request.POST)
#         if form.is_valid():
#             # try:
#                 # Catalog.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddProdForm()
#     return render(request, 'catalog/add.html', {'form': form, 'menu': menu, 'title': 'Добавление продукта'})

 
 
def login(request):
    return HttpResponse("Авторизация")


class CatalogHome(ListView):
    model = Catalog
    template_name = 'catalog/index.html'
    context_object_name = 'product'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, **kwargs):   #*, object_list=None,
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['product'] = Catalog.objects.all()
        context['categs'] = Category.objects.all()
        context['categ_selected'] = 0
        return context


# def index(request):
#     product = Catalog.objects.all()
#     categs = Category.objects.all()
#     context = {'product': product,
#                 'categs': categs,
#                 'menu': menu, 
#                 'title': 'Главная',
#                 'categ_selected': 0,
#             }
#     return render(request, 'catalog/index.html', context=context)


# def login(request):
#     return HttpResponse('Авторизация')

# def product(request):
#     return HttpResponse('product')


def show_product(request, product_id):
    # print(request.GET)
    product = get_object_or_404(Catalog, pk=product_id)
    categs = Category.objects.all()
    
    context = {'product': product,
                'categs': categs,
                'menu': menu, 
                'title': 'Категории',
                'categ_selected': product.categ_id,
            }
    return render(request, 'catalog/product.html', context=context)


class ShowCategory(ListView):
    model = Catalog
    template_name = 'catalog/index.html'
    context_object_name = 'product'
    # extra_context = {'title': 'Главная'}

    def get_queryset(self):
        return Catalog.objects.filter(categ__id=self.kwargs['categ_id'], is_published=True)

    def get_context_data(self, **kwargs):   #*, object_list=None,
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['product'] = Catalog.objects.all()
        context['categs'] = Category.objects.all()
        # context['categ_selected'] = Catalog.objects.filter(categ__id=self.kwargs['categ_id'])
        # context['categ_selected'] = context['categs'][0].categ_id
        return context

# def show_category (request, categ_id):
#     product = Catalog.objects.filter(categ_id=categ_id)
#     categs = Category.objects.all()

#     if len(product) == 0:
#         raise Http404()

#     context = {'product': product,
#                 'categs': categs,
#                 'menu': menu, 
#                 'title': 'Категории',
#                 'categ_selected': categ_id,
#             }
#     return render(request, 'catalog/index.html', context=context)


# def contact(request):
#     return HttpResponse("Обратная связь")

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")