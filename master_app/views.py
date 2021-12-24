from django.shortcuts import render
from .models import  Blogvillage ,Blogaccomodation ,Blogtransportation,Blogname, Blogtext
from django.http import Http404

# Create your views here.



def index(request):
    return render(request, 'index.html')

def blogpage(request):
    blogs=Blogvillage.objects.all()
    blogsa=Blogaccomodation.objects.all()
    blogstr=Blogtransportation.objects.all()
    blogsn = Blogname.objects.all()
    blogst = Blogtext.objects.all()
    print(blogs)
    context={
        "blogs":blogs,
        "blogsa":blogsa,
        "blogstr":blogstr,
        "blogsn":blogsn,
        "blogst":blogst
    }
    return render(request, 'blogpage.html',context)




