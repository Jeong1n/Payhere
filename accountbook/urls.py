from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.accountView.as_view()),
    path('account/<int:obj_id>/copy/', views.AccountCopyInstance.as_view()),
    path('account/<int:obj_id>/', views.accountView.as_view()),
    path('', views.accountView.as_view()),
    path('put/<int:obj_id>/', views.accountView.as_view()),
    path('delete/<int:obj_id>/', views.accountView.as_view()),
    path('<int:obj_id>', views.accountView.as_view()),
    path('detail/<int:obj_id>/', views.DetailView.as_view()),
]