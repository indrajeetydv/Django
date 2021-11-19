from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Employee


# Create your views here.
def createView(request):
    return render(request, 'create.html')

def store(request):
    emp=Employee()
    emp.name=request.POST.get('emp_name')
    emp.email=request.POST.get('emp_email')
    emp.mobile=request.POST.get('emp_mobile')
    emp.save()
    messages.success(request,"Employee added successfully")
    return redirect('/create')

def index(request):
    emp=Employee.objects.all()
    return render(request,'index.html',{'employees':emp})

def viewEmp(request,pk):
   emp = Employee.objects.get(id = pk)
   return render(request, 'view.html',{'employee':emp})

def deleteEmp(request, pk):
    emp = Employee.objects.get(id = pk)
    emp.delete()
    messages.success(request, "Employee Deleted Successfully")
    return redirect('/')

def updateView(request,pk):
    emp = Employee.objects.get(id = pk)
    return render(request,'update.html',{'employee':emp})

def update(request,pk):
    print('in')
    emp = Employee.objects.get(id = pk)
    emp.name = request.POST.get('emp_name')
    emp.email = request.POST.get('emp_email')
    emp.mobile = request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Update Successfully")
    return redirect('/')