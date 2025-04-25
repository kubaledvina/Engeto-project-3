# Volební scraper

Tento Pythonový projekt slouží ke stažení výsledků parlamentních voleb z webu volby.cz a jejich uložení do CSV souboru.
Skript stáhne seznam obcí z vybrané stránky okrsku, následně projde každou obec a uloží pro ni volební data – celkové počty 
registrovaných voličů, účast, platné hlasy a výsledky pro jednotlivé politické strany.

## Verze Python 3.12.10

## Import knihoven

Projekt vyžaduje importovat tyto knihovny:

- requests
- beautifulsoup4
- csv
- sys

Můžeš je nainstalovat přes pip:

pip install -r requirements.txt


## Spuštění

Pusť skript v příkazové řádce pomocí:

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vysledky_budejce.csv"

- URL musí být v uvozovkách. 
- Výstupní soubor bude CSV obsahující hlavičku a jeden řádek za každou obec s jejími výsledky.


## Popis hlavních funkcí
- get_html(link) – stáhne HTML obsah stránky

- get_links(soup) – získá odkazy na jednotlivé obce

- id_towns(soup) – stáhne kódy obcí

- name_towns(soup) – stáhne názvy obcí

- politics_parties(soup) – stáhne názvy politických stran

- get_vote(soup) – stáhne údaje o počtu registrovaných voličů, obálek a platných hlasů

- collect_votes(soup) – stáhne počty hlasů pro strany v jednotlivých obcích

- scraper(url, filename) – hlavní funkce, která koordinuje stažení a zápis dat

## Ukázka běhu programu

.......

Downloading data from: https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=531049&xvyber=2101.

Saving data to file: vysledky_budejce.csv

Exit program: main.py


## Struktura CSV

- Kód obce

- Název obce

- Registrovaní voliči

- Vydané obálky

- Platné hlasy

- Počty hlasů pro každou politickou stranu




## Ukázka výstupu
code,location,registred,envelopes,valid,ODS,ČSSD,Piráti,...

533928,BEDŘICHOV,123,100,98,30,25,20,...

533936,DUBÍ,456,400,390,110,90,80,...

...


