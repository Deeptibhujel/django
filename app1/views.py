from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Student 

def hello(request):
    students = Student.objects.all()
    context = {
        "S": students            #S is key
    }
    return render (request, "app1/index.html",context)

def hi (request):
    context = {
        "user_info":{
            "name":"Deepti",
            "age": 18,
            "location":"chhorepatan",
        },
        "hobbies":{
            "indoor":["reading","coding","gaming"],
            "outdoor":["hiking","cycling","swimming"],
        },
        "greeting":{
            "message":"Hello,Welcome to my profile!",
            "timestamp":"2081-06-07 10:57 am",
        },
        
    }
        
    
    return render(request, "app1/index.html", context)