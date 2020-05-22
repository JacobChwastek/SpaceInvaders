opis_SpaceInvaders

# Opis projektu z **Języków Symbolicznych**
# Chwastek Jakub
## Opis zadania:
Stworzenie gry przypominającej popularną grę ** Space Invaders **
przy wykorzystaniu bilioteki **Pygame**. Gra powinna zawierać:

1. **Definicje**
	
	- **gracz** - osoba uruchamiająca aplikacje, kontrolująca statek z pomocą strzałek i klawiasza spacja
	- **statek gracz** - obiekt znajdujący się na dole wyrenderowanego ekranu. Podlega kontroli przez gracza. 
	- **statki przeciwników** - obiektu generowane w górej częsci ekranu. Poruszające się w sposób niezależny od gracza.
	- **pocisk** - obiekt wystrzeliwany ze statku gracza w kierunku pionowym z punktem początkowym zgodnym z współrzędnymi statku gracza
	- **mina** - obiekt generowany z losową częstotliwością z losowych przeciwników w kierunku pionowy w kierunku gracza.
	- **poziom** - ustawiony przez system poziom trudności zdefiniowany jako zmienna wpływająca między innymi na prędkość i ilość przeciwników oraz częstotliwość wystrzeliwanych min 
	- **menu** - ekran renderowany przez apliakcję ukazujący podstawowe możliwości dla gracza między innymi przycisk umożliwiający rozpoczęcie gry.
	- **liczba puntków** - puntky generowane względem ilości zniszczonych przecinków * współczynnik trudności
	- **bunkier ** - obiekt tworzony przez aplikacje jego zadaniem jest ochrona przez pociskami przeciwnika. W momecie kolizji z miną statku przeciwnika. Bunkier ulega częściowemu zniszczeniu, aż do całkowitej likwidacji

2. **Cel gry**
	Celem gry jest zdobycie jak największej ilości puntków przez gracza poprzez niszczenie statków przecinika na poszczególnych poziomach
3. **Przypadki testowe**
	**Scenariusz 1. Uruchomienie aplikacji** 
		Opis: Gracz pomyślnie uruchomi aplikację
		Wymagania: brak
		Kroki:
			1. Gracz uruchamia aplikację 
			2. Pokazuje się menu z dostępnymi przyciskami Start i Zakończ
			3. Gracz klika przycisk 'Start'
			4. Gracz przenoszony jest do ekranu gry 
	**Scenariusz 2. Ruch statkiem gracza**
		Opis: Statek gracza porusza się jedynie w lewo lub prawo podczas używania przez gracza klawiszy strzałek. Obiekt nie powinien reagować na inne klawisze strzałek. Obiekt nie wyjeżdza poza ekran gry.
		Wymagania: Gracz wybrał w Menu opcje 'Start'
		Kroki:
			1. Gracz klika klawisz prawej strzałki
				1.1 Statek gracza wykonuje ruch w wyznaczonym kierunku, aż do momentu dotarcia do ekranu gry
			2.Gracz klika klawisz lewej strzałki
				2.1 Statek gracza porusza się w wyznaczonym kierunku, aż do momentu dotarcia do ekranu gry
			3. Gracz klika pozostałe klawisze strzałek
				3.1 Statek gracza nie reaguje
		Opis: Statek gracza po naciśnieciu klawiasza SPACJA wystrzeliwuje pocisk
		Wymagania: Uruchomiona gra
		Kroki:
			1.Gracz porusza się w wybraną pozycję statkiem.
			2.Gracz klika klawisz SPACJI
			2.1 Statek wystrzeliwuje pocisk w kierunku pionowym
			2.2 Współrzędna X pocisku jest stała i zgodna z pozycja statku gracza w momecie wystrzelnia pocisku
			2.3. Współrzędna Y pocisku ulega stałemu zmiejszeniu co jest równoznaczne z stałym poruszaniem się pocisku w kierunku pionowym (w rozumieniu gracza do góry)
			3. Gracz posiada możliwość wystrzelenia kolejengo pocisku tylko jeżeli poprzedni dotarł w krawędzi ekranu lub dochodzi do kolizji z statkiem przeciwnka.
	**Scenariusz 4. Zniszczenie statku przeciwnika:**
		Opis: W momencie kontatku pocisku gracza z statkiem przeciwnika powinno dość do unicestwienia statku gracza i doliczenia odpowieniej ilości punktów do sumy punktów uzyskanych przez gracza
		Wymagania: Uruchomina gra
		Kroki:
		1. Statek gracza wystrzeliwuje pocisk
		2. Pocisk trafia w statek przeciwnika
		3. Statek przeciwnika ulega zniszczeniu
		4. Liczba puntków gracza zostaje zwiększona
		5. Gracz niszczy wszystkich przeciwników
		6. Gracz przechodzi na kolejny poziom
		7. Generowani są nowi przeciwnicy w wyżsyzm stopniu trudności
**Scenariusz 5. Zniszczenie statku gracza w skutek kolizji z miną**
		Opis: Pocisk przeciwniak trafia w gracza
		Wymagania: Uruchomiona gra
		Kroki: 
		1. Statek przeciwnika generuje miną 
		2. Bomba trafia statek gracza
		3. Gra jest resetowana
		4. Na ekranie pojawia sie komuniakt *Koniec gry wynik: XXX* oraz klawisze *Koniec* oraz *Zagraj jeszcze raz*
		
**Scenariusz 6. Zniszczenie statku gracza w skutek kolizji z przeciwnikiem**
		Opis: Gra powinna dopuszcza w którym w momencie dotarcia statków przeciwnków do pozycji gracza gra ulega zakonczeniu
		Wymagania: Uruchomiona gra
		Kroki:
		1. Statki przeciwnika poruszają się stopniowo w kierunku gracza
		2. Gracz nie oddaje wystarczajacej ilości celnych strzałów
		3. Dochodzi do kolizji miedzy statkiem przecinika oraz stakiem gracza
		3. Lub statek gracza dotyka krawędzi dolnego ekranu
		4. Gra jest resetowana
		5. Na ekranie pojawia sie komuniakt *Koniec gry wynik: XXX* oraz klawisze *Koniec* oraz *Zagraj jeszcze raz*
		
**Scenariusz 7 Zniszczenie bunkru**
		Opis: W momencie kolizcji statku przeciwnika z bunkrem lub miną bunkier powinien ulec częściowemu lub całkowitemy zniszczeniu
		Wymagania: Uruchomiona gra. Bunkier nie ejst juz zniszczony.
		Kroki:
		1. Statek przeciwnika generuje minę 
		2. Mina poruszą się w kierunku pionowym
		3. Na drodze mina stoi bunkier
		4. W miejscu kolizji dochodzi do usunięcia fragementu bunkra
**Scenariusz 8 *Nowy Pomysł* Tabela wyników**
	Opis: gracz w menu powinien miec możliwosc wybrania możliwość tabela wyników która wyswietli ranking uprzednio uzysaknych wyników. Wynik po kazdej grze powinien byc dodawany do bazy danych lub plik tekstowego.
	Kroki: Gracz jest w menu. Gracz rozegrał wczesniej wiecej niz jeden mecz.
	Kroki:
	1. Gracz jest w menu 
	2. gracz wybiera opcję tabela wyników
	3. Graczowi pokazuje się tabela wyswietlajaca uporządkowaną listę uzyskanych przez niego wyników 
		
		
		
