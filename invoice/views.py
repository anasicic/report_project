from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
import json
import os


@login_required
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
        # U slučaju da datoteka ne postoji, postavljamo prazne liste za podatke
        data = {"TypeOfCost": [], "CostCenter": [], "Supplier": []}

        # Pozivamo vašu Django management komandu za popunjavanje baze podataka
        call_command('my_command')

    # Prikazivanje podataka u predlošku
    return render(request, 'invoice/home.html', {'data': data})