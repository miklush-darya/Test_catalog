from django.urls import path
from .views import CatalogHome, ShowCategory, AddPage
# 
from .views import about, login
# from .views import show_category, index, addpr
# from .views import *

urlpatterns = [
    
    path('', CatalogHome.as_view(), name='home'),
    # path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    # path('addpage/', addpr, name='add_page'),
    # path('contact/', contact, name='contact'),
    # path('catalog/', catalog, name = "catalog"), 
    path('login/', login, name='login'),
    path('category/<int:categ_id>/', ShowCategory.as_view(), name='category'),
    # path('category/<int:categ_id>/', show_category, name='category'),
]