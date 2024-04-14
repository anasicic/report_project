from django.db import models

class TypeOfCost(models.Model):
	cost_code = models.IntegerField()
	cost_name = models.CharField(max_length=40)


class CostCenter(models.Model):
	cost_center_code = models.IntegerField()
	cost_center_name = models.CharField(max_length=40)


class Supplier(models.Model):
	supplier_name = models.CharField(max_length=40)

	