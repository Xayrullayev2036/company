from django.urls import path

from branch import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('branches/list/',views.BranchesListView.as_view(),name='branches-list'),
    path('branches/create/',views.BranchesCreateView.as_view(),name='branches-create'),
    path('branches/<int:pk>/update',views.BranchesUpdateView.as_view(),name='branches-update'),
    path('branches/<int:pk>/detail/',views.BranchesDetailView.as_view(),name='branches-detail'),
    path('branches/<int:pk>/delete/',views.branches_delete,name='branches-delete'),
]