from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView
)

from department.models import Department
from employee.models import Employee
from employee.forms import EmployeeForm
from profession.models import Profession


class IndexView(TemplateView):
    template_name = "index.html"

class EmployeesListView(ListView):
    model = Employee
    template_name = "employee_html/list.html"
    context_object_name = "employees"


    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        gender =self.request.GET.get('gender')
        profession_id = self.request.GET.get('profession_id')
        department_id = self.request.GET.get('department_id')

        if search:
            queryset = queryset.filter(
                Q(first_name__contains = search) | Q(last_name__contains = search) | Q(age__gt = search)
            )
        if gender:
            queryset = queryset.filter(
                gender = gender
            )
        if profession_id:
            queryset = queryset.filter(
                profession_id=profession_id
            )
        if department_id:
            queryset = queryset.filter(
                department_id=department_id
            )
        return queryset


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context["professions"] = Profession.objects.all()
        context["departments"] = Department.objects.all()

        context["search"] = self.request.GET.get("search","")
        context["gender"] = self.request.GET.get("gender")
        profession_id = self.request.GET.get("profession_id","")
        department_id = self.request.GET.get("department_id","")
        if profession_id:
            profession_id = int(profession_id)
        else:
            profession_id = 0
        if department_id:
            department_id = int(department_id)
        else:
            department_id = 0
        context["profession_id"] = profession_id
        context["department_id"] = department_id

        return context

class EmployeesCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee_html/form.html"
    success_url = "/employees/list/"




class EmployeesUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee_html/form.html"
    success_url = "/employees/list/"

class EmployeesDetailView(DetailView):
    model = Employee
    template_name = "employee_html/detail.html"
    context_object_name = "employees"

def employees_delete(request,pk):
    employees = get_object_or_404(Employee,pk=pk)
    employees.delete()
    return redirect("authors-list")