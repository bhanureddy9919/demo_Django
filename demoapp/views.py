from django.shortcuts import render


#  ************
from django.http import HttpResponse

from .models import Blog
# from .models import Contact
# Create your views here.

def homeapp(request):
    post=Blog.objects.all()
    return render(request, "base.html",{'post':post})

def demoapp(request):
    if request.method=='POST':
        title=request.POST['title']
        author=request.POST['author']
        description=request.POST['description']
        image=request.FILES.get('image')
        
        k=Blog(title=title,author=author,description=description,image=image)
        k.save()
    return render(request,"demopage.html")
