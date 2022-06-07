from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(Request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dict={'insert_me':"hello help"}
    return render(request,'ProTwo/help.html',context=my_dict)
