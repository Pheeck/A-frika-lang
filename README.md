# A-frika-lang

Z runických zápisů na jakémsi džunglovém papyru se povedlo vyčíst prazvláštní programovací jazyk. Experti si lámou hlavu s tím, jak byli divoši, kteří nikdy neviděli jediný počítač, schopni něco takového vytvořit. Jeho fungování bylo však již rozluštěno a interpret implementovaný v pythonu je k dispozici zde.


### Usage

`./afrika.py program.af`


### Syntax

Každý program operuje na nekonečně velkém paměťovém poli. Pomocí následujících instrukcí lze operovat s paměťovým a instrukčním ukazatelem, lze číst a vypisovat znaky a inkrementovat nebo dekrementovat jednotlivé buňky pole.

| Instrukce | Popis                                                        |
| --------- | ------------------------------------------------------------ |
| `A. A?`   | Posun ukazatele na následující buňku paměťového pole         |
| `A? A.`   | Posun ukazatele na předchozí buňku paměťového pole           |
| `A. A.`   | Inkrementace aktivní paměťové buňky o 1                      |
| `A! A!`   | Dekrementace aktivní paměťové buňky o 1                      |
| `A. A!`   | Uložení hodnoty ze vstupu do aktivní buňky (kódované v ASCII) |
| `A! A.`   | Výpis hodnoty z aktivní buňky na výstup (kódované v ASCII)   |
| `A! A?`   | Pokud je hodnota aktivní buňky rovna nule, provede přesun ukazatele dopředu za odpovídající `A? A!` |
| `A? A!`   | Pokud je hodnota aktivní buňky různá od nuly, provede přesun ukazatele dozade před odpovídající `A! A?` |

### Komenty

Jakékoliv znaky, které nejsou součástí jakékoliv instrukce interpret ignoruje.

### Hello World!!

hello.af
```
A. A? A. A. A. A. A. A. A. A. A. A. A. A. A. A.
A. A. A. A. A! A? A? A. A. A. A. A. A. A. A. A.
A. A. A. A. A. A. A. A. A. A? A! A! A? A! A? A.
A! A. A. A? A. A. A. A. A. A. A. A. A. A. A. A.
A. A. A! A? A? A. A. A. A. A. A. A. A. A. A. A?
A! A! A? A! A? A. A. A. A! A. A. A. A. A. A. A.
A. A. A. A. A. A. A. A. A! A. A! A. A. A. A. A.
A. A. A! A. A. A? A. A? A. A? A. A. A. A. A. A.
A. A. A. A. A. A. A. A. A. A. A! A? A? A. A. A.
A. A. A. A. A. A. A. A? A! A! A? A! A? A. A! A.
A. A? A. A? A. A? A. A. A. A. A. A. A. A. A. A.
A. A. A. A. A. A. A. A. A. A. A! A? A? A. A. A.
A. A. A. A. A. A. A. A. A. A. A. A. A. A. A. A.
A. A? A! A! A? A! A? A. A! A! A! A! A! A! A! A.
A? A. A? A. A? A. A? A. A! A. A. A. A. A. A. A.
A! A. A! A! A! A! A! A! A! A! A! A! A! A! A! A.
A! A! A! A! A! A! A! A! A! A! A! A! A! A! A! A!
A! A. A. A? A. A? A. A. A! A.
```