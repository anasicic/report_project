from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.db.models import Sum
from invoice.models import Invoice, TypeOfCost, CostCenter
import openpyxl
from django.http import HttpResponse
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render, get_object_or_404

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
            expenses_by_center[cost_center] = total_amount or 0  # Dodavanje ukupnog iznosa u rječnik
        expenses_by_type_and_center[type_of_cost] = expenses_by_center

    return render(request, 'users/report.html', {'expenses_by_type_and_center': expenses_by_type_and_center})


def export_to_excel(request):
    types_of_cost = TypeOfCost.objects.all()
    cost_centers = CostCenter.objects.all()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Expense Report'

    
    headers = ['Type of cost'] + [cc.cost_center_name for cc in cost_centers]
    sheet.append(headers)

    
    for type_of_cost in types_of_cost:
        row = [type_of_cost.cost_name]
        for cost_center in cost_centers:
            expenses = Invoice.objects.filter(cost_code=type_of_cost, cost_center_code=cost_center)
            total_amount = expenses.aggregate(total_amount=Sum('netto_amount'))['total_amount'] or 0
            row.append(total_amount)
        sheet.append(row)

    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=cost_report.xlsx'
    workbook.save(response)
    return response

def cost_chart(request, type_of_cost_id):
    selected_type_of_cost = get_object_or_404(TypeOfCost, pk=type_of_cost_id)
    
    
    cost_centers = CostCenter.objects.all()
    
    
    labels = []
    amounts = []
    
    for cost_center in cost_centers:
        expenses = Invoice.objects.filter(cost_code=selected_type_of_cost, cost_center_code=cost_center)
        total_amount = expenses.aggregate(total_amount=Sum('netto_amount'))['total_amount'] or 0
        labels.append(cost_center.cost_center_name)
        amounts.append(total_amount)
    
    plt.figure(figsize=(12, 6))
    plt.bar(labels, amounts)
    plt.xlabel('Cost Centers')
    plt.ylabel('Total Cost (EUR)')
    plt.title(f'Expense Distribution for {selected_type_of_cost.cost_name}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    graphic = base64.b64encode(image_png).decode('utf-8')
    image_src = f'data:image/png;base64,{graphic}'
    
    return render(request, 'users/cost_chart.html', {'image_src': image_src})