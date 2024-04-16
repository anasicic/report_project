from django.shortcuts import render
from .models import TypeOfCost, CostCenter, Supplier

def home(request):
    types_of_cost = TypeOfCost.objects.all()
    cost_centers = CostCenter.objects.all()
    suppliers = Supplier.objects.all()

    return render(request, 'invoice/home.html', {'types_of_cost': types_of_cost, 'cost_centers': cost_centers, 'suppliers': suppliers})