from django.shortcuts import render, redirect, get_object_or_404
from .models import TypeOfCost, CostCenter, Supplier, Invoice
from django.contrib.auth.decorators import login_required
from .forms import InvoiceForm  # Uvozimo formu za stvaranje računa
from django.contrib import messages



@login_required
def home(request):
    types_of_cost = TypeOfCost.objects.all()
    cost_centers = CostCenter.objects.all()
    suppliers = Supplier.objects.all()
    user_invoices = Invoice.objects.filter(user=request.user)

    # Ako je korisnik admin, prikazujemo sve račune
    if request.user.is_staff or request.user.is_superuser:
        user_invoices = Invoice.objects.all()
    else:
        # Ako nije admin, prikazujemo samo njegove račune
        user_invoices = Invoice.objects.filter(user=request.user)

    return render(request, 'invoice/home.html', {'types_of_cost': types_of_cost, 'cost_centers': cost_centers, 'suppliers': suppliers, 'invoices': user_invoices, 'show_username': request.user.is_staff or request.user.is_superuser})


@login_required
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.user = request.user  # Postavljanje trenutnog korisnika kao vlasnika računa
            invoice.save()
            messages.success(request, 'Invoice successfully created.')
            return redirect('invoice-home')
        else:
            messages.error(request, 'Form is not valid. Please check your input.')
    else:
        form = InvoiceForm()
    return render(request, 'invoice/create_invoice.html', {'form': form})


@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice/invoice_detail.html', {'invoice': invoice})

@login_required
def delete_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == 'POST' and 'confirm_delete' in request.POST:
        invoice.delete()
        messages.success(request, 'Invoice deleted successfully.')
        return redirect('invoice-home')

    return render(request, 'invoice/confirm_delete.html', {'invoice': invoice})

@login_required
def delete_invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            invoice.delete()
            messages.success(request, 'Invoice deleted successfully.')
            return redirect('invoice-home')
        else:
            messages.info(request, 'Invoice deletion canceled.')
            return redirect('invoice-detail', pk=invoice.pk)

    return render(request, 'invoice/confirm_delete.html', {'invoice': invoice})

@login_required
def update_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            # Promjena formata datuma
            date = form.cleaned_data['date']
            formatted_date = date.strftime("%Y-%m-%d")  # Novi format datuma
            form.cleaned_data['date'] = formatted_date  # Ažuriranje datuma u formi

            form.save()
            return redirect('invoice-detail', pk=pk)
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoice/update_invoice.html', {'form': form})


