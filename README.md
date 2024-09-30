# Report Project

**Report Project** je web aplikacija temeljena na MTV (Model-Template-View) arhitekturi, izrađena u Djangu. Aplikacija omogućava unos ulaznih računa i izvještavanje o ukupnim troškovima po mjestima troška.

## Sadržaj

- [Pokretanje servera](#pokretanje-servera)
- [Struktura aplikacije](#struktura-aplikacije)
- [Funkcionalnosti](#funkcionalnosti)
- [Tehnologije](#tehnologije)

---

## Pokretanje servera

Kako biste pokrenuli projekat lokalno, pratite sledeće korake:

1. **Klonirajte repozitorij**:

    Ako projekat preuzimate sa GitHub-a, klonirajte repozitorij koristeći `git clone`:

    ```bash
    git clone https://github.com/anasicic/report_project.git
    ```


2. **Idite u direktorij projekta**:

    Nakon što je projekt kloniran, uđite u direktorij projekta:

    ```bash
    cd report_project
    ```

3. **Instalirajte potrebne pakete**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Stvorite migracijske datoteke za bazu podataka**:

    ```bash
    python manage.py makemigrations
    ```

5. **Izvršite migraciju kako biste primijenili promjene u bazi podataka**:

    ```bash
    python manage.py migrate
    ```

6. **Pokrenite razvojni server**:

    ```bash
    python manage.py runserver
    ```

7. **Otvorite preglednik i idite na**:

    ```url
    http://127.0.0.1:8000/
    ```

---

## Struktura aplikacije

Aplikacija se sastoji od dvije aplikacije: `invoice` i `users`. Obje aplikacije nasljeđuju `base.html`, u kojem je definiran kostur svih stranica.

- **Baza podataka**: Aplikacija koristi SQLite za pohranu podataka.
- **Frontend**: Frontend je izrađen pomoću HTML, CSS i Bootstrap.

### Invoice aplikacija

- Sadrži četiri modela: 
  - `TypeOfCost`
  - `CostCenter`
  - `Supplier`
  - `Invoice`

- Model `Invoice` je međutablica koja povezuje ostale modele, uključujući i korisnika (User).

---

## Funkcionalnosti

### 1. Prijava korisnika

- Pri pokretanju aplikacije, korisnicima se prikazuje sučelje za prijavu (Login).
- Neregistrirani korisnici mogu se registrirati putem forme na linku "Register".
- **Funkcionalnost**: Korisnička autentifikacija (prijava, registracija, odjava).

### 2. Administratorske ovlasti

- Administrator može pristupiti sučelju za dodavanje/brisanje korisnika, dobavljača, vrsta troškova i mjesta troškova.
- **Funkcionalnost**: Administratorske funkcije (dodavanje i brisanje korisnika, generiranje izvještaja).

### 3. Prikaz popisa ulaznih računa

- Prikazuje broj računa, datum, dobavljača i netto iznos.
- Administratori vide dodatno i korisnika koji je unio račun.

### 4. Ažuriranje i brisanje računa

- Nakon ažuriranja ili brisanja računa, korisnik dobiva poruku o uspjehu i vraća se na početnu stranicu.

### 5. Dodavanje novog računa

- Korisnici mogu unositi nove račune putem forme na početnoj stranici.

### 6. Korisnički profil

- Korisnici mogu ažurirati svoje podatke putem stranice "Profile".

### 7. Odjava

- Korisnik se može odjaviti klikom na "Logout".

---

## Tehnologije

- **Django** - Web framework za backend
- **SQLite** - Baza podataka
- **HTML, CSS, Bootstrap** - Frontend tehnologije za izradu sučelja

