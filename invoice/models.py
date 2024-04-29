from django.db import models
from django.contrib.auth.models import User

class TypeOfCost(models.Model):
	cost_code = models.IntegerField()
	cost_name = models.CharField(max_length=40)
	def __str__(self):
	   return f"{self.cost_code} - {self.cost_name}"



class CostCenter(models.Model):
	cost_center_code = models.IntegerField()
	cost_center_name = models.CharField(max_length=40)
	def __str__(self):
	   return f"{self.cost_center_code} - {self.cost_center_name}"
	


class Supplier(models.Model):
	supplier_name = models.CharField(max_length=40)
	
	def __str__(self):
         return self.supplier_name

class Invoice(models.Model):
    cost_code = models.ForeignKey(TypeOfCost, on_delete=models.CASCADE)
    cost_center_code = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    netto_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    invoice_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
	    return f"{self.invoice_number}  {self.date.strftime('%d.%m.%Y')}  {self.supplier.supplier_name}  {self.netto_amount}"