from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import get_object_or_404,redirect
from django.db.models import Q
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView
)

from branch.models import Branch
from department.forms import DepartmentForm
from department.models import Department

class IndexView(TemplateView):
    template_name = 'index.html'


class DepartmentsListView(ListView):
    model = Department
    template_name = 'department_html/list.html'
    context_object_name = "departments"



    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        head = self.request.GET.get('head')
        branch_id = self.request.GET.get('branch_id')

        if search:
            queryset = queryset.filter(
                Q(name__contains = search) | Q(description__contains = search)
            )
        if head:
            queryset = queryset.filter(
                head = head
            )
        if branch_id:
            queryset = queryset.filter(
                branch_id = branch_id
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["branches"] = Branch.objects.all()

        context["search"] = self.request.GET.get('search',"")
        branch_id = self.request.GET.get('branch_id',"")
        if branch_id:
            branch_id = int(branch_id)
        else:
            branch_id = 0
        context["branch_id"] = branch_id

        return context


class DepartmentsCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = '/departments/list/'
    template_name = 'department_html/form.html'

class DepartmentsUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    success_url = '/departments/list'
    template_name = 'department_html/form.html'

class DepartmentsDetailView(DetailView):
    model = Department
    template_name = 'department_html/detail.html'
    context_object_name = "departments"

def departments_delete(request,pk):
    departments = get_object_or_404(Department,pk=pk)
    departments.delete()
    return redirect("departments-list")
