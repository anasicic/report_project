from django.shortcuts import render
import json
import os

def home(request):
    # Dobivanje apsolutne putanje do datoteke seed_data.json
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(SITE_ROOT, "seed_data.json")
    

    # Provjera postoji li datoteka
    if os.path.isfile(file_path):
        # Učitavanje podataka iz datoteke
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
    else:
        # Ako datoteka ne postoji, postavljamo prazne liste za podatke
        data = {"TypeOfCost": [], "CostCenter": [], "Supplier": []}

    # Prikazivanje podataka u predlošku invoice/home.html
    return render(request, 'invoice/home.html', {'data': data})