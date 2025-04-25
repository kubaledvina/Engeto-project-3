"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Jakub Ledvina
email: ledvinajakub@seznam.cz
"""


import requests
from bs4 import BeautifulSoup
import csv
import sys


def get_html(link):
    """
    Načte HTML stránku ze zadaného odkazu a vrátí ji jako objekt BeautifulSoup.

    :param link: URL adresa webové stránky
    :return: objekt BeautifulSoup s HTML obsahem stránky
    """
    try:
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            print(f"Downloading data from: {link}.")
            return soup
        else: print(f"Error. Status code: {response.status_code}")
        return None

    except requests.RequestException as e:
        print(f"Error downloading data: {e}.")
        return None


def argv_link():
    """
    Získá HTML obsah stránky ze zadaného odkazu pomocí argumentů z příkazové řádky.

    :return: objekt BeautifulSoup s HTML obsahem stránky
    """

    if len(sys.argv) == 3:
        links = get_html(sys.argv[1])
        return links
    else:
        print("You entered the wrong number of arguments. The arguments must be 3."
          "File name, url in quotation marks and any name of the output .csv.")
        quit()


def id_towns(links) -> list:
    """
    Získá ID měst (číselné kódy obcí) z HTML stránky okrsku.

    :param links: HTML stránka okrsku (BeautifulSoup)
    :return: seznam ID měst jako řetězce (např. ["533928", "533936", ...])
    """
    id_t = [i.text.strip() for i in links.find_all("td", class_="cislo")]
    return id_t


def name_towns(links) -> list:
    """
    Získá názvy měst z HTML stránky okrsku.

    :param links: HTML stránka okrsku (BeautifulSoup)
    :return: seznam názvů měst jako řetězce
    """

    name_t = [n.text.strip() for n in links.find_all("td", class_="overflow_name")]
    return name_t


def get_links(links) -> list:
    """
    Získá odkazy na podstránky jednotlivých obcí z HTML stránky okrsku.

    :param links: HTML obsah okrsku (BeautifulSoup)
    :return: seznam URL adres podstránek obcí
    """

    path = []
    link_search = links.find_all("td", class_="cislo")

    for td in link_search:
        a_tag = td.find("a")
        if a_tag:
            href = a_tag.get("href")
            path.append(f"https://www.volby.cz/pls/ps2017nss/{href}")
    return path


def politics_parties(links) -> list:
    """
    Získá názvy politických stran z první obce ve výpisu.

    :param links: HTML stránka hlavního okrsku (BeautifulSoup)
    :return: seznam názvů politických stran
    """

    town_link = get_links(links)
    html = requests.get(town_link[0])
    html_villages = BeautifulSoup(html.text, "html.parser")
    parties = [p.text.strip() for p in html_villages.find_all("td", class_="overflow_name")]
    return  parties


def get_vote(links) -> tuple[list[str], list[str], list[str]] | None:
    """
    Získá počty registrovaných voličů, volební účast a počet platných hlasů pro všechny obce.

    :param links: HTML obsah okrsku (BeautifulSoup)
    :return: trojice seznamů: (voters, attendance, valid_ones)
     """

    voters = []
    attendance = []
    valid_ones = []

    path = get_links(links)
    for p in path:
        html_village = BeautifulSoup(requests.get(p).text, "html.parser")
        voters.extend([v.text.replace("\xa0", " ") for v in html_village.find_all("td", headers="sa2")])
        attendance.extend([a.text.replace("\xa0", " ") for a in html_village.find_all("td", headers="sa3")])
        valid_ones.extend([o.text.replace("\xa0", " ") for o in html_village.find_all("td", headers="sa6")])

    return voters, attendance, valid_ones


def collect_votes(links) -> list:
    """
    Vrátí počty hlasů pro každou stranu ve všech obcích.

    Pro každý odkaz na obec stáhne HTML, najde buňky s hlasy a uloží je do seznamu.

    :return: list: Seznam seznamů s počty hlasů jako text.
    """
    links = get_links(links)
    votes = []

    for link in links:
        html = get_html(link)
        votes_search = html.find_all("td", headers=["t1sb3", "t2sb3"])
        temp = [v.text.replace("\xa0", " ") for v in votes_search]
        votes.append(temp)

    return votes

def rows_creator(links) -> list:
    """
    Vytvoří seznam řádků pro zápis do CSV souboru.

    Každý řádek obsahuje: ID obce, název obce, počet registrovaných voličů, volební účast,
    počet platných hlasů a počty hlasů pro jednotlivé strany.

    :param links: HTML obsah okrsku (BeautifulSoup)
    :return: seznam řádků pro zápis do CSV
    """

    voters, attendance, valid_ones = get_vote(links)
    towns = name_towns(links)
    idt = id_towns(links)
    votes = collect_votes(links)

    aux_var = [[i, t, v, a, vo] for i, t, v, a, vo in zip(idt, towns, voters, attendance, valid_ones)]
    rows = [av + vs for av, vs in zip(aux_var, votes)]

    return rows


def scraper(links, file):
    """
    Hlavní funkce pro scrapování dat z webu volby.cz a uložení výsledků do CSV souboru.

    :param links: URL adresa hlavní stránky okrsku
    :param file: název výstupního CSV souboru
    """

    try:
        soup = get_html(links)
        header = ['code', 'location', 'registred', 'envelopes', 'valid']
        content = rows_creator(soup)
        parties = politics_parties(soup)

        if not content or not parties:
            raise ValueError("No data to write to CSV.")

        print("Saving data to file:", file)
        for party in parties:
            header.append(party)

        with open(file, mode='w', encoding='utf-8', newline='') as f:
            f_writer = csv.writer(f)
            f_writer.writerow(header)
            f_writer.writerows(content)

        print("Exit program:", sys.argv[0])
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    address = sys.argv[1]
    file_name = sys.argv[2]
    scraper(address, file_name)