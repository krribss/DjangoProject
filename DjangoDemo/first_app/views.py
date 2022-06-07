from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
print(2)
def index(request):
    my_dict={'insert_me': "hello I am from Views.py 1"}
    return render(request,'first_app/index.html',context=my_dict)
