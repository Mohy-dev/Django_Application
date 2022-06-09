from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm

# REST_FRAMEWORK
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer


# rest_framework views.
@api_view(['GET'])
def api_all_students(request):
    all_st = Student.objects.all()
    sr_serializer = StudentSerializer(all_st, many=True)
    return Response(sr_serializer.data)


# Rest Functions
@api_view(['GET'])
def api_student_details(request, st_id):
    all_st = Student.objects.get(id=st_id)
    sr_serializer = StudentSerializer(all_st, many=False)
    return Response(sr_serializer.data)


@api_view(['POST'])
def api_student_create(request):
    sr_serializer = StudentSerializer(data=request.data)
    if sr_serializer.is_valid():
        sr_serializer.save()
    return redirect('api-list')


@api_view(['POST'])
def api_student_edit(request, st_id):
    st = Student.objects.get(id=st_id)
    sr_serializer = StudentSerializer(instance=st, data=request.data)
    if sr_serializer.is_valid():
        sr_serializer.save()
    return redirect('api-list')


@api_view(['DELETE'])
def api_student_delete(request, st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return Response('User Deleted Successfully')


##################
def home(request):
    student = Student.objects.all()
    context = {"all_st": student}
    return render(request, "djapp/home.html", context)


def work(request):
    return HttpResponse("Work")


def hello(request, st_id):
    st = Student.objects.get(id=st_id)
    st_name = st.first_name
    return HttpResponse(st_name)


def show(request, st_id):
    st = Student.objects.get(id=st_id)
    context = {"st": st}
    return render(request, "djapp/show.html", context)


def deleteStudent(request, st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return redirect('home')


def editStudent(request, st_id):
    student = Student.objects.get(id=st_id)
    st_form = StudentForm(instance=student)

    if request.method == 'POST':
        st_form = StudentForm(request.POST, instance=student)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context = {'form': st_form}
    return render(request, 'djapp/add-student.html', context)


def addStudent(request):
    if request.method == 'POST':
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    st_form = StudentForm()
    context = {'form': st_form}
    return render(request, 'djapp/add-student.html', context)
