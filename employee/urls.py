from django.urls import path
from . import views

urlpatterns = [
    #employee urls
    path('employee_list', views.employee_list, name='employee_list'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('<int:pk>/employee_update/', views.employee_update, name='employee_update'),
    path('<int:pk>/employee_delete/', views.employee_delete, name='employee_delete'),
]


