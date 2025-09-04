from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages

# Custom login view with auto-register
def custom_login(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Try to create the user if not exists
            try:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('index')
            except Exception as e:
                messages.error(request, 'Login failed. Please try a different username.')
    return render(request, 'custom_login.html')
# Home page view
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income, Expense
from django.utils import timezone


@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    return render(request, 'income_list.html', {'incomes': incomes})

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def add_income(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Income.objects.create(user=request.user, amount=amount, description=description, date=date)
        return redirect('income_list')
    return render(request, 'add_income.html')

@login_required
def add_expense(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Expense.objects.create(user=request.user, amount=amount, description=description, date=date)
        return redirect('expense_list')
    return render(request, 'add_expense.html')
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')        

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')