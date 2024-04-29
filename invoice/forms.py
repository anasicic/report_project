from django import forms
from .models import Invoice, TypeOfCost, Supplier, CostCenter

class InvoiceForm(forms.ModelForm):
    # Dodaj padajući izbornik za cost_code
    cost_code = forms.ModelChoiceField(queryset=TypeOfCost.objects.all(), empty_label='')
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label='')
    cost_center_code = forms.ModelChoiceField(queryset=CostCenter.objects.all(), empty_label='')
    date = forms.DateField(label='Date (DD.MM.YYYY)', input_formats=['%d.%m.%Y'])


    class Meta:
        model = Invoice
        fields = ['invoice_number', 'date', 'supplier', 'cost_code', 'cost_center_code', 'netto_amount'] 