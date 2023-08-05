from django.urls import path

from department import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('departments/list/',views.DepartmentsListView.as_view(),name='departments-list'),
    path('departments/create/',views.DepartmentsCreateView.as_view(),name='departments-create'),
    path('departments/<int:pk>/update',views.DepartmentsUpdateView.as_view(),name='departments-update'),
    path('departments/<int:pk>/detail/',views.DepartmentsDetailView.as_view(),name='departments-detail'),
    path('departments/<int:pk>/delete/',views.departments_delete,name='departments-delete'),
]