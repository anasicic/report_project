from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.db.models import Sum
from invoice.models import Invoice, TypeOfCost, CostCenter





def register(request):
	if request.method =="POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f'Your account has been created! You are now able to log in')
			login(request, user)
			return redirect('invoice-home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def profile(request):
    user = request.user
    if user.is_staff or user.is_superuser:
        return redirect('admin:index')  
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserRegisterForm(instance=user)
    
    return render(request, 'users/profile.html', {'form': form})


def report(request):
    types_of_cost = TypeOfCost.objects.all()
    cost_centers = CostCenter.objects.all()

    expenses_by_type_and_center = {}  

    for type_of_cost in types_of_cost:
        expenses_by_center = {} 
        for cost_center in cost_centers:
            
            expenses = Invoice.objects.filter(cost_code=type_of_cost, cost_center_code=cost_center)
            
            total_amount = expenses.aggregate(total_amount=Sum('netto_amount'))['total_amount']
            expenses_by_center[cost_center] = total_amount or 0  # Dodavanje ukupnog iznosa u rečnik
        expenses_by_type_and_center[type_of_cost] = expenses_by_center

    return render(request, 'users/report.html', {'expenses_by_type_and_center': expenses_by_type_and_center})
