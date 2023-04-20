from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def insert_page_view(request):
    return render(request, "app/insert.html")


def insert_data(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        contact = request.POST['contact_number']
  
   

    # creating object of Model class
    # insert data into student table

    new_student = Student.objects.create(
        first_name=fname, last_name=lname, email=email, contact_number=contact)
    
    return redirect('show')


#Show page view
def show_data(request):
    #select * from table name
    students = Student.objects.all()

    return render(request,"app/show.html",{"student":students})



def insert2(request):
    return render(request, "app/insert2.html")

#Edit Page view

def edit_data(request,pk):
    #fetching the data of particular ID
    get_data = Student.objects.get(id=pk)
    return render(request,'app/edit.html',{'key2':get_data})

#update data view

def update_data(request,pk):
    std_data = Student.objects.get(id=pk)
    std_data.first_name = request.POST['first_name']
    std_data.last_name = request.POST['last_name']
    std_data.email = request.POST['email']
    std_data.contact_number = request.POST['contact_number']
    #query for update

    std_data.save()
    return redirect('show')

#delete data

def delete_data(request,pk):
    #fetching the data of particular ID
    d_data = Student.objects.get(id=pk)
    d_data.delete()
    return redirect('show')

   