from django.shortcuts import render, redirect
from .models import  Blogdetails
from django.http import Http404
from .forms import addblog

# Create your views here.



def index(request):
    return render(request, 'index.html')

def blogpage(request):


    blogs = Blogdetails.objects.all()
    print(blogs)
    context={
        "blogs":blogs,

    }
    return render(request, 'blogpage.html',context)

def addblogpage(request):
    if request.method == 'POST' :
        add_form = addblog(request.POST)

        if add_form.is_valid():
            add_form.save()

            return redirect('index')
        else:
            print(add_form.errors)

    else:
        add_form = addblog()

    context = {"add_form": add_form}

    return render(request, "addblogpage.html", context)




