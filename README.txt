report_project

Pokretanje servera

1. Otvorite Command Prompt (CMD) i idite u direktorij vašeg projekta:
   cd "putanja_do_vašeg_projekta"

2. Instalirajte potrebne pakete:
   pip install -r requirements.txt

3. Stvorite migracijske datoteke za bazu podataka:
   python manage.py makemigrations

4. Izvršite migraciju kako biste primijenili promjene u bazi podataka:
   python manage.py migrate

5. Pokrenite razvojni server:
   python manage.py runserver

6. Otvorite preglednik i idite na:
   http://127.0.0.1:8000/


report_project je web aplikacija temeljena na MTV (Model-Template-View) arhitekturi, izrađena u Djangu.

Za pohranu podataka koristi SQLite bazu podataka, dok se fronted bazira na HTML, CSS i Bootstrap.

Aplikacija omogućava unos ulaznih računa i izvještavanje o ukupnim troškovima po mjestima troška.

Projekt se sastoji od dvije aplikacije: invoice i users. Obje aplikacije nasljeđuju base.html, u kojem je definiran kostur svih stranica.


Aplikacija invoice sastoji se od četiri modela: class TypeOfCost, class CostCenter, class Supplier, class Invoice.

Class Invoice je međutablica koja povezaju sve ostale modele, uključujući i User-a.


Tijek aplikacije

1. Prijava korisnika:

- Prilikom pokretanja projekta prikazuje se sučelje za prijavu (Login).
- Neregistrirani korisnici mogu kliknuti na "Register" i ispuniti formu za registraciju.
- Nakon uspješne registracije, korisnik je preusmjeren na početnu stranicu (home view) koja prikazuje popis ulaznih računa iz baze podataka.

2. Administratorske ovlasti:

- Administrator, uz sve opcije dostupne običnim korisnicima, može pristupiti administratorskom sučelju preko linka Profile
- Preko administratorskog sučelja može dodavati i brisati korisnike, dobavljače, vrste troškova i mjesta troškova.
- Administrator ima pristup linku "Report" koji prikazuje ukupne troškove po mjestima troška.

3. Prikaz popisa ulaznih računa:

- Popis ulaznih računa sadrži broj računa, datum, dobavljača, netto iznos i, za administratore, korisnika koji je unio račun.
- Klikom na broj određenog računa otvara se prikaz detalja računa (invoice_detail view) s opcijama "Update" i "Delete".

4. Ažuriranje i brisanje računa:

- Nakon ažuriranja podataka korisnik se vraća na početnu stranicu s porukom o uspješnom ažuriranju.
- Pri brisanju računa korisniku se prikazuje potvrda, a nakon brisanja vraća se na početnu stranicu s porukom o uspješnom brisanju.

5. Dodavanje novog ulaznog računa:

- Na početnoj stranici korisnik može kliknuti na "Add New Invoice" za unos novog ulaznog računa.
- Otvara se forma za unos podataka. Ako nisu ispunjeni obavezni podaci, korisnik dobiva poruku o obaveznom polju.
- Klikom na "Save" korisnik se vraća na početnu stranicu gdje se prikazuje novi ulazni račun.

6. Korisnički profil:

- Na početnoj stranici obični korisnik ima link "Profile" koji prikazuje formu s podacima o korisniku.
- Korisnik može ažurirati svoje podatke putem ove forme.

7. Odjava korisnika:

- Korisnik se može odjaviti klikom na "Logout" kako bi izašao iz aplikacije.






