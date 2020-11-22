from datetime import timezone,time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import *

#base

def basepage (request):
    list = shop.objects.all()
    imagee= shop.image.field

    listshop={
        "list" :list


    }
    return render(request,"shop/index.html",listshop)

#page(404 and about)
def about (request):
    return render(request,'shop/about.html')

def error (request):
    return render(request,'shop/404.html')

#index view

def index(request):
    best = shop.objects.all().order_by(time).filter()
    context={
        'best':best
    }
    return render(request,'shop/index.html')

#company

class companyListView(ListView):
    model = company
    template_name = 'shop/company.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'companys'  # Default: object_list
    paginate_by = 2
    queryset = company.objects.all()  # Default: Model.objects.all()
#company_view
def company_view (request,code):
    queri = company.objects.get(id=code)
    context={
        "queri":queri
    }
    return render(request,"shop/company_view.html",context)
#shop
class shopListView(ListView):
    model = shop
    template_name = 'shop/shop.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'shops'  # Default: object_list
    paginate_by = 2
    queryset = shop.objects.all()  # Default: Model.objects.all()
#shop_view

def shop_view(request,code):
    queri= shop.objects.get(id=code)
    context={
        'queri':queri
    }
    return render(request,"shop/shop_view.html",context)




#salessite
class salessiteListView(ListView):
    model = shop
    template_name = 'shop/salessite.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'list'  # Default: object_list
    paginate_by = 2
    queryset = shop.objects.all()  # Default: Model.objects.all()

#salessite_view
def salessite_view(request,code):
    queri=salessite.objects.filter(id=code)
    shopp = shop.objects.get(salessite=code)
    context={
        'queri':queri,
        'shopp':shopp
    }
    return render(request,"shop/salessiteview.html",context)





#fuckpage
def fuck (request):
    list=shop.objects.all()
    context={
        'list':list
    }
    return render(request, 'shop/home.html', context)