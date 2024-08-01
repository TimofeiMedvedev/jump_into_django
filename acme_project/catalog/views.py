# catalog/views.py
from django.http import HttpResponse

def product_category(request, category):    
    return HttpResponse(f'Категория {category}') 