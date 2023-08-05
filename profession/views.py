from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import(
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    CreateView
)

from profession.models import Profession
from profession.forms import ProfessionForm




class IndexView(TemplateView):
    template_name = "index.html"


class ProfessionsListView(ListView):
    model = Profession
    template_name = "profession_html/list.html"
    context_object_name = "professions"


    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        salary = self.request.GET.get('salary')
        profession_id = self.request.GET.get('profession_id')

        if search:
            queryset = queryset.filter(
                Q(name__contains = search) | Q(description__contains = search)
            )
        if salary:
            queryset = queryset.filter(
                salary = salary
            )
        if profession_id:
            queryset = queryset.filter(
                profession_id = profession_id
            )
        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context["professions"] = Profession.objects.all()

        context["search"] = self.request.GET.get("search")
        context["salary"] = self.request.GET.get("salary")
        profession_id = self.request.GET.get("profession_id")
        if profession_id:
            profession_id = int(profession_id)
        else:
            profession_id = 0
        context["profession_id"] = profession_id

        return context

class ProfessionsCreateView(CreateView):
    model = Profession
    form_class = ProfessionForm
    template_name = "profession_html/form.html"
    success_url = "/professions/list/"

class ProfessionsUpdateView(UpdateView):
    model = Profession
    form_class = ProfessionForm
    template_name = "profession_html/form.html"
    success_url = "/professions/list/"

class ProfessionsDetailView(DetailView):
    model = Profession
    template_name = "profession_html/detail.html"
    success_url = "/professions/list/"

def professions_delete(request,pk):
    professions = get_object_or_404(Profession,pk=pk)
    professions.delete()
    return redirect('professions-list')
