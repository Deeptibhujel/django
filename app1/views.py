from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Student 
from .forms import StudentForm

def hello(request):
    students = Student.objects.all()
    context ={"S": students}            #S is key 
    return render (request, "app1/index.html",context)

def create_student(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    
    return render(request, 'app1/create_student.html',context)

# def hi (request):
#     context = {
#         "user_info":{
#             "name":"Deepti",
#             "age": 18,
#             "location":"chhorepatan",
#         },
#         "hobbies":{
#             "indoor":["reading","coding","gaming"],
#             "outdoor":["hiking","cycling","swimming"],
#         },
#         "greeting":{
#             "message":"Hello,Welcome to my profile!",
#             "timestamp":"2081-06-07 10:57 am",
#         },
        
#     }
        
    
#     return render(request, "app1/index.html", context)