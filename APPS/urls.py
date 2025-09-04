
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('income/', views.income_list, name='income_list'),
    path('expense/', views.expense_list, name='expense_list'),
    path('income/add/', views.add_income, name='add_income'),
    path('expense/add/', views.add_expense, name='add_expense'),
]
