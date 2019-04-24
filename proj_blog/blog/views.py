from django.shortcuts import render
from .models import *
from django.http import HttpResponse
authors=[{'author_name':'Vasudha Sood','book':'New_book1'
    },{'author_name':'John','book':'New_book2'
    }]
post=[{'Post_name':'Hello World',
           'Created':'12 April 2019'},
          {'Post_name':'Hello World1',
           'Created':'11 April 2019'}]
# Create your views here.
def home(request):

    context={'posts': Post.objects.all()}

    return render(request,"blog/home.html",context)
def about(request):
    return render(request, "blog/about.html",{'title':'About_Page'})