from django.contrib import admin
from .models import Supplier, CostCenter, TypeOfCost

admin.site.register(Supplier)
admin.site.register(CostCenter)
admin.site.register(TypeOfCost)

# Register your models here.
