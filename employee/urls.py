from django.urls import path

from employee import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('employees/list/',views.EmployeesListView.as_view(),name='employees-list'),
    path('employees/create/',views.EmployeesCreateView.as_view(),name='employees-create'),
    path('employees/<int:pk>/update',views.EmployeesUpdateView.as_view(),name='employees-update'),
    path('employees/<int:pk>/detail/',views.EmployeesDetailView.as_view(),name='employees-detail'),
    path('employees/<int:pk>/delete/',views.employees_delete,name='employees-delete'),
]