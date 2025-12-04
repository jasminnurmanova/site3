from django.shortcuts import render
from django.http import HttpResponse
from .models import Markazlar,Category

def home_page(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'home_page.html',context)

def markazlar_func(request,pk):
    markazlar=Markazlar.objects.filter(category__id=pk)
    context={'markazlar': markazlar}
    return render(request,'markazlar.html',context)

def detail_markazlar(request,pk):
    markazlar=Markazlar.objects.filter(pk=pk).first()
    print(111, markazlar)
    return render(request,'details.html',{'markazlar':markazlar})
