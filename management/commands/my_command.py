import json
from django.core.management.base import BaseCommand
from invoice.models import TypeOfCost, CostCenter, Supplier

class Command(BaseCommand):
    help = 'Generira seed podatke iz JSON datoteke i sprema ih u bazu podataka'

    def handle(self, *args, **kwargs):
        file_name = "seed_data.json"

        with open(file_name) as json_file:
            data = json.load(json_file)

            for item in data.get('TypeOfCost', []):
                TypeOfCost.objects.create(cost_code=item['cost_code'], cost_name=item['cost_name'])

            for item in data.get('CostCenter', []):
                CostCenter.objects.create(cost_center_code=item['cost_center_code'], cost_center_name=item['cost_center_name'])

            for item in data.get('Supplier', []):
                Supplier.objects.create(supplier_name=item['supplier_name'])

        self.stdout.write(self.style.SUCCESS('Podaci uspješno zapisani u bazu.'))