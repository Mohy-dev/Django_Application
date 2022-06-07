from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student


def home(request):
    student = Student.objects.all()
    context = {"all_st": student}
    return render(request, "djapp/home.html", context )
    

def work(request):
    return HttpResponse("Work")

def hello(request, st_id):
    st = Student.objects.get(id = st_id)
    st_name = st.first_name
    return HttpResponse(st_name)

def show(request, st_id):
    st = Student.objects.get(id = st_id)
    context = {"st": st}
    return render(request, "djapp/show.html", context )

def deleteStudent(request, st_id):
    st = Student.objects.get(id = st_id)
    st.delete()
    return redirect('home')