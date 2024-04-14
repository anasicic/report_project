import json
from invoice.models import TypeOfCost, CostCenter, Supplier


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


file_name = "seed_data.json"


with open(file_name, "w") as json_file:
    json.dump(data,json_file,indent=4)