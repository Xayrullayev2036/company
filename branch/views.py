from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import(
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView
)

from branch.forms import BranchForm
from branch.models import Branch


class IndexView(TemplateView):
    template_name = "index.html"

class BranchesListView(ListView):
    model = Branch
    template_name = "branch_html/list.html"
    context_object_name = "branches"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__contains=search) | Q(location__contains=search) | Q(manager__contains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Branch.objects.all()
        context["search"] = self.request.GET.get('search',"")
        return context


class BranchesCreateView(CreateView):
    model = Branch
    form_class = BranchForm
    success_url = "/branches/list/"
    template_name = "branch_html/form.html"

class BranchesUpdateView(UpdateView):
    model = Branch
    form_class = BranchForm
    success_url = "/branches/list/"
    template_name = "branch_html/form.html"

class BranchesDetailView(DetailView):
    model = Branch
    template_name = "branch_html/detail.html"
    context_object_name = "branches"

def branches_delete(request,pk):
    branches = get_object_or_404(Branch,pk=pk)
    branches.delete()
    return redirect("branches-list")