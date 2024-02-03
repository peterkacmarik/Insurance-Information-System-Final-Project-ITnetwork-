# Informačný systém poistených

Tento repozitár obsahuje implementáciu informačného systému pre správu poistených osôb. Systém je napísaný v jazyku Python a umožňuje základné operácie ako pridávanie, vyhľadávanie, úpravu a odstraňovanie záznamov poistených osôb.

## Štruktúra kódu

Kód je rozdelený do niekoľkých tried, ktoré sú popísané nižšie:

1. **UserDatabase**: Trieda na správu databázy poistených osôb.
2. **UserManagement**: Trieda na správu operácií s poistencami, ako je vytváranie nových záznamov.
3. **ManageInsured**: Trieda na vyhľadávanie, úpravu a odstraňovanie existujúcich záznamov poistených osôb.
4. **Insured**: Trieda reprezentujúca jednotlivého poisteného.

## Funkcie programu

- **Pridanie nového poisteného**: Umožňuje vytvorenie nového záznamu poisteného vrátane kontroly správnosti vstupných údajov.
- **Zoznam všetkých poistencov**: Zobrazuje zoznam všetkých poistencov v databáze.
- **Vyhľadávanie poistených osôb**: Umýšľa používateľovi vyhľadať poistenú osobu podľa kritérií.
- **Úprava údajov poistených osôb**: Umožňuje úpravu existujúcich záznamov poistených osôb.
- **Odstránenie poistených osôb**: Umožňuje odstránenie existujúcich záznamov poistených osôb z databázy.

## Spustenie programu

Pre spustenie programu vykonajte súbor `menu.py`. Po spustení sa zobrazí hlavné menu, kde môžete vybrať požadovanú akciu zadanie čísla od 1 do 6.

## Licencia

Tento projekt je licencovaný pod [MIT licenciou](LICENSE).
