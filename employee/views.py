from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def index(request):
    return render(request,'index.html')
# def add(request):
#     return render(request, 'add.html')

#     if request.method == "POST":

#         employee_id = request.POST.get('employee_id')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         department = request.POST.get('department')
#         designation = request.POST.get('designation')
#         salary = request.POST.get('salary')
#         address = request.POST.get('address')

#         Employee.objects.create(
#             employee_id=employee_id,
#             name=name,
#             email=email,
#             phone=phone,
#             department=department,
#             designation=designation,
#             salary=salary,
#             address=address
#         )

#         return redirect('view')

#     return render(request, 'add.html')
def add(request):

    if request.method == "POST":

        

        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        address = request.POST.get('address')

        Employee.objects.create(
            employee_id=employee_id,
            name=name,
            email=email,
            phone=phone,
            department=department,
            designation=designation,
            salary=salary,
            address=address
        )

        

        return redirect('view')

    return render(request, 'add.html')

def view(request):
    employees = Employee.objects.all()

    return render(request,'view.html',{'employees': employees})

def edit(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.employee_id = request.POST.get('employee_id')
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.department = request.POST.get('department')
        employee.designation = request.POST.get('designation')
        employee.salary = request.POST.get('salary')
        employee.address = request.POST.get('address')

        employee.save()

        return redirect('view')

    return render(
        request,'edit.html', {'employee': employee})

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        employee.delete()
        return redirect('view')

    return redirect('view')