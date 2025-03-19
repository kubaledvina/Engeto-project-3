#  Tic Tac Toe - Python Console Game

Tento projekt byl vytvořen jako **druhý projekt v Engeto kurzu - Python Akademie**.\
Jedná se o klasickou hru **Piškvorky (Tic Tac Toe)** pro dva hráče.

---

##  Pravidla hry

- Hráči se střídají v zadávání čísel **(1-9)**, které odpovídají polím na hrací desce **3x3**.
- Hráč vybere číslo odpovídající volnému poli a jeho symbol (`X` nebo `O`) se tam umístí.
- Hra končí, pokud některý hráč umístí **3 své symboly za sebou** (horizontálně, vertikálně nebo diagonálně).
- Pokud se zaplní všechna pole a nikdo nevyhraje, hra končí **remízou**.
- **Sleduje se čas hry**: na konci hry se zobrazí jak dlouho trvala hra.

---

##  Použitá knihovna

- `time` (pro měření délky hry)

---

## Struktura kódu

- `playing_board(board)`: Zobrazí hrací desku.
- `check_game(board, player)`: Kontroluje, zda hráč vyhrál.
- `draw(board)`: Zjišťuje, zda je hra remízou.
- `tic_tac_toe()`: Hlavní smyčka hry.

---

##  Jak spustit hru

1. Stáhni soubor **`main.py`**.
2. Otevři terminál ve složce se souborem.
3. Spusť příkaz:
   ```sh
   py main.py
   ```

---

##  Ukázka hry

```
Welcome to Tic Tac Toe
==============================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
==============================
Let's start the game
------------------------------
Player X | Please enter your move number (1-9): 
```


