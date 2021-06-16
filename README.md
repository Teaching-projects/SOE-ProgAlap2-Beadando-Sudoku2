# SOE-ProgAlap2-Beadando-Sudoku2
Farkas Mirjam

# Sudoku
A program egy megszokott suduku játék. 9x9 táblát kell feltölteni 1-9-ig számokkal a következő feltételek alapján (a sudoku szabályai alapján): -egy sorban az adott számból csak 1 lehet -egy oszlopban az adott számból csak 1 lehet -a 9x9 táblát további 9 kis kockára osztjuk, ahol egy-egy kockában csak 1-1 lehet az adott számból.

# Even or odd
Ez a páros vagy páratlan játékmód annyiban különbözik az alap sudoku szabályaitól, hogy a páros vagy páratlan mezők be vannak "satírózva", ezekben a mezőkben csak páros vagy csak páratlan számok lehetnek.

# A Játékról
A játék elindulásakor egy menüt láthatunk, amelyben kiválaszthatjuk a játszani kivánt nehézségi fokot, illetve játémódot.

Kiválasztás után a legenerált táblát láthatjuk valamint, hogy hányat hibázhatunk még és segítséget mennyi segítséget kérhetünk. Ez a tábla tetején található. A tábla jobb oldalán találhatjuk a beírni kivánt számokat(1-9-ig). Először a tábla adott pozíciójára kell kattintanunk, majd a beírni kivánt számra. Ha rossz számot írnánk be, akkor elveszítünk egy hibapontot, illetve piros színnel láthatjuk a táblán. Az alap számokat nem lehet módosítani még a kézzel beírtakat bármikor lehet. A tábla sikeres megoldása után egy "gratulálok, nyertél!" üzenetet kapunk, majd ezt bezárva a program befejeződik. A tábla sikertelen megoldása után (elértük a maximálisan megengedett hiba számot) egy "Sajnálom vesztettél!" üzenetet láthatunk, majd ezt bezárva a program befelyeződik.

# A programról
4 file-ban található a program. 

A main.py felelős a program futtatásáért.

A game.py-ban található található maga az alap logika, a tábla randomizált legenerálása, a segítségek, életek megadása, valamint a kezdő tábla készítése. A legnagyobb nehézséget a tábla generálása okozta. eleinte 200 ezer próbálkozásból sem talált egy helyes táblát sem. Ezt egy "keresztes" megoldással küszöböltem ki, ami alatt azt értem, hogy először középre kenerálok 9 random számot, majd ahhoz viszonyítva generálom a többi 3x3 négyzetet. Először keresztbe generálok, majd a maradék 4 3x3-as négyzetet töltöm ki. 
A program rögtön ellenőriz, ha be kerül egy szám a táblába. Ezt egy összehasonlító függvénnyel hajtom végre. Összenézem az alap generált táblával.

evenorodd.py-ban található a külön játémód, amely örökli a game.py generálását kiegészítve azt a generálással.

Az ui.py felelős a grafikus megjelenítésért. 