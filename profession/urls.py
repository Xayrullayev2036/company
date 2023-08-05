from django.urls import path

from profession import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('professions/list/',views.ProfessionsListView.as_view(),name='professions-list'),
    path('professions/create/',views.ProfessionsCreateView.as_view(),name='professions-create'),
    path('professions/<int:pk>/update',views.ProfessionsUpdateView.as_view(),name='professions-update'),
    path('professions/<int:pk>/detail/',views.ProfessionsDetailView.as_view(),name='professions-detail'),
    path('professions/<int:pk>/delete/',views.professions_delete,name='professions-delete'),
]