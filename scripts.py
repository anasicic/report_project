import json
from invoice.models import TypeOfCost, CostCenter, Supplier
from django.db import connection

def reset_sequence(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}'")

def generate_seed_data():
    # Provjeri postoji li već podaci u bazi
    if TypeOfCost.objects.exists() or CostCenter.objects.exists() or Supplier.objects.exists():
        print("Baza podataka već sadrži podatke. Ne treba ih ponovno generirati.")
        return

    # Definiraj podatke koji će se upisati u bazu i generirati JSON datoteku
    data = {
        "TypeOfCost": [
            {"cost_code": 400400, "cost_name": "Office supplies"},
            {"cost_code": 400100, "cost_name": "Electricity"},
        ],
        "CostCenter": [
            {"cost_center_code": 11, "cost_center_name": "Marketing"},
            {"cost_center_code": 15, "cost_center_name": "Management"},
        ],
        "Supplier": [
            {"supplier_name": "Office Source"},
            {"supplier_name": "Energo"},
        ]
    }

    # Resetiranje ID-ova na 1 ako su tablice prazne
    TypeOfCost.objects.all().delete()
    CostCenter.objects.all().delete()
    Supplier.objects.all().delete()

    # Resetiranje sekvenci ID-ova
    reset_sequence(TypeOfCost._meta.db_table)
    reset_sequence(CostCenter._meta.db_table)
    reset_sequence(Supplier._meta.db_table)

    # Lista za čuvanje objekata koje ćemo dodati u bazu
    objects_to_create = []

    # Kreiranje objekata za dodavanje u bazu
    for item in data.get('TypeOfCost', []):
        obj = TypeOfCost(cost_code=item['cost_code'], cost_name=item['cost_name'])
        objects_to_create.append(obj)

    for item in data.get('CostCenter', []):
        obj = CostCenter(cost_center_code=item['cost_center_code'], cost_center_name=item['cost_center_name'])
        objects_to_create.append(obj)

    for item in data.get('Supplier', []):
        obj = Supplier(supplier_name=item['supplier_name'])
        objects_to_create.append(obj)

    # Masovno dodavanje objekata u bazu
    TypeOfCost.objects.bulk_create(objects_to_create[:2])
    CostCenter.objects.bulk_create(objects_to_create[2:4])
    Supplier.objects.bulk_create(objects_to_create[4:])

    # Generiranje JSON datoteke
    file_name = "seed_data.json"
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Podaci uspješno upisani u bazu i generirana JSON datoteka.")

# Poziv funkcije za generiranje JSON datoteke i punjenje baze
generate_seed_data()
