from django.core.management.base import BaseCommand
from invoice.models import TypeOfCost, CostCenter, Supplier
import json
import os

class Command(BaseCommand):
    help = 'Popunjava bazu podacima iz JSON datoteke'

    def handle(self, *args, **kwargs):
        # Definirajte apsolutnu putanju do datoteke seed_data.json
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "seed_data.json")

        # Provjera postoji li datoteka seed_data.json
        if os.path.isfile(file_path):
            # Učitavanje podataka iz datoteke
            with open(file_path, "r") as json_file:
                data = json.load(json_file)

                # Unos podataka u bazu samo ako već nisu prisutni
                for item in data.get('TypeOfCost', []):
                    TypeOfCost.objects.get_or_create(cost_code=item['cost_code'], defaults={'cost_name': item['cost_name']})

                for item in data.get('CostCenter', []):
                    CostCenter.objects.get_or_create(cost_center_code=item['cost_center_code'], defaults={'cost_center_name': item['cost_center_name']})

                for item in data.get('Supplier', []):
                    Supplier.objects.get_or_create(supplier_name=item['supplier_name'])

            self.stdout.write(self.style.SUCCESS('Podaci uspješno uneseni u bazu.'))

        else:
            self.stdout.write(self.style.WARNING('Datoteka seed_data.json nije pronađena.'))