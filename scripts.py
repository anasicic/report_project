import json
from invoice.models import TypeOfCost, CostCenter, Supplier

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

    # Upisivanje podataka u bazu
    for item in data.get('TypeOfCost', []):
        TypeOfCost.objects.create(cost_code=item['cost_code'], cost_name=item['cost_name'])

    for item in data.get('CostCenter', []):
        CostCenter.objects.create(cost_center_code=item['cost_center_code'], cost_center_name=item['cost_center_name'])

    for item in data.get('Supplier', []):
        Supplier.objects.create(supplier_name=item['supplier_name'])

    # Generiranje JSON datoteke
    file_name = "seed_data.json"
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Podaci uspješno upisani u bazu i generirana JSON datoteka.")

# Poziv funkcije za generiranje JSON datoteke i punjenje baze
generate_seed_data()

    