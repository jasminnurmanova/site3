
from django.shortcuts import render,redirect
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

def create_markaz(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        category=Category.objects.filter (type= request.POST.get('category','')).first()
        created_at=request.POST.get('created_at','')
        location=request.POST.get('location','')
        print(location)
        desc=request.POST.get('desc','')
        image=request.FILES.get('image')

        markaz = Markazlar.objects.create(
            name=name,
            category=category,
            created_at=created_at,
            location=location,
            desc=desc,
            image=image
        )
        markaz.save()
        return redirect('details', markaz.pk)

    return render(request,'create_markaz.html')



def update_markaz(request,pk):
    markaz=Markazlar.objects.filter(pk=pk).first()
    if request.method == 'POST':
        markaz.name=request.POST.get('name','')
        markaz.category=Category.objects.filter (type= request.POST.get('category','')).first()
        markaz.created_at=request.POST.get('created_at','')
        markaz.location=request.POST.get('location','')
        markaz.desc=request.POST.get('desc','')
        markaz.image=request.FILES.get('image')


        markaz.save()
        return redirect('details', markaz.pk)

    return render(request,'update_markaz.html',{'markaz':markaz})