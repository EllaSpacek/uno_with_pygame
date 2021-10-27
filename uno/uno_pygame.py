# UNO-Spiel mit Pygame
# Ein menschlicher Spieler und 1-5 Computergegner
# Eingaben per Tastatur
# Work in process...

# To-Do:

# 1. 
# - Statistiken ausgeben (sind vorbereitet)
# - Möglichkeit neues Spiel zu beginnen -> Mit Ja/Nein-Abfrage
# - Regeln erkläre -> Zu Beginn, evtl mit Pop-up-Fenster?

# 2. 
# ein bisschen intelligenz einbauen - Computergegner wählt nicht random, sondern wählt z.B. Farben, die er häufig auf der Hand hat
# Karten sortieren -> das eigene Deck ordnen, macht strategisches Spielen einfacher
# Programm-Ablauf-Diagramm -> Statt des rein textbasierten Ablaufplans
# Englisch als Sprache auswählen -> Zu Beginn, auslagern in andere Datei



import pygame  # Modul um Spiele zu programmieren
import sys  # um das Programm vollständig zu beenden
import random

############################ Karten - Klassen, Objekte und Kartenstapel erstellen ################################

# Karten-Klassen

class Karte:
    # Alle Kartenarten erben von dieser Klasse
    def __init__(self, farbe, image):
        self.farbe = farbe
        self.image = image

class ZahlenKarte(Karte):
    # Bunte Karten mit Zahlen, keine Wirkungen
    def __init__(self, farbe, image, zahl):
        super().__init__(farbe, image)
        self.zahl = zahl

class SonderKarte(Karte):
    # Haben keine Zahlen, aber Wirkungen, können bunt oder schwarz sein
    def __init__(self, farbe, image, wirkung):
        super().__init__(farbe, image)
        self.wirkung = wirkung
        self.genutzt = False  # Ob die Wirkung bereits genutzt wurde

# nötige Variablen, um Karten zu erstellen

# Bilder
# Für Zahlenkarten
farben = ['blau', 'gelb', 'grün', 'rot']
img_blau_zahlen = ['uno_images/zahlenkarten/blau/blau_null_neu.jpg', 'uno_images/zahlenkarten/blau/blau_eins_neu.jpg', 'uno_images/zahlenkarten/blau/blau_zwei_neu.jpg', 'uno_images/zahlenkarten/blau/blau_drei_neu.jpg', 'uno_images/zahlenkarten/blau/blau_vier_neu.jpg', 'uno_images/zahlenkarten/blau/blau_fuenf_neu.jpg', 'uno_images/zahlenkarten/blau/blau_sechs_neu.jpg', 'uno_images/zahlenkarten/blau/blau_sieben_neu.jpg', 'uno_images/zahlenkarten/blau/blau_acht_neu.jpg', 'uno_images/zahlenkarten/blau/blau_neun_neu.jpg']
img_gelb_zahlen = ['uno_images/zahlenkarten/gelb/gelb_null_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_eins_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_zwei_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_drei_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_vier_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_fuenf_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_sechs_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_sieben_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_acht_neu.jpg', 'uno_images/zahlenkarten/gelb/gelb_neun_neu.jpg']
img_gruen_zahlen = ['uno_images/zahlenkarten/gruen/gruen_null_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_eins_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_zwei_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_drei_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_vier_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_fuenf_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_sechs_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_sieben_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_acht_neu.jpg', 'uno_images/zahlenkarten/gruen/gruen_neun_neu.jpg']
img_rot_zahlen = ['uno_images/zahlenkarten/rot/rot_null_neu.jpg', 'uno_images/zahlenkarten/rot/rot_eins_neu.jpg', 'uno_images/zahlenkarten/rot/rot_zwei_neu.jpg', 'uno_images/zahlenkarten/rot/rot_drei_neu.jpg', 'uno_images/zahlenkarten/rot/rot_vier_neu.jpg', 'uno_images/zahlenkarten/rot/rot_fuenf_neu.jpg', 'uno_images/zahlenkarten/rot/rot_sechs_neu.jpg', 'uno_images/zahlenkarten/rot/rot_sieben_neu.jpg', 'uno_images/zahlenkarten/rot/rot_acht_neu.jpg', 'uno_images/zahlenkarten/rot/rot_neun_neu.jpg']

# Für bunte Sonderkarten
wirkungen_bunt = ['plus 2', 'Richtungswechsel', 'Aussetzen']
img_wirkungen_blau = ['uno_images/sonderkarten/farben/blau_plus_zwei_neu.jpg', 'uno_images/sonderkarten/farben/blau_richtungswechsel_neu.jpg', 'uno_images/sonderkarten/farben/blau_aussetzen_neu.jpg']
img_wirkungen_gelb = ['uno_images/sonderkarten/farben/gelb_plus_zwei_neu.jpg', 'uno_images/sonderkarten/farben/gelb_richtungswechsel_neu.jpg', 'uno_images/sonderkarten/farben/gelb_aussetzen_neu.jpg']
img_wirkungen_gruen = ['uno_images/sonderkarten/farben/gruen_plus_zwei_neu.jpg', 'uno_images/sonderkarten/farben/gruen_richtungswechsel_neu.jpg', 'uno_images/sonderkarten/farben/gruen_aussetzen_neu.jpg']
img_wirkungen_rot = ['uno_images/sonderkarten/farben/rot_plus_zwei_neu.jpg', 'uno_images/sonderkarten/farben/rot_richtungswechsel_neu.jpg', 'uno_images/sonderkarten/farben/rot_aussetzen_neu.jpg']

# Für schwarze Sonderkartem
wirkungen_schwarz = ['plus 4', 'Farbe wünschen']
img_wirkungen_schwarz = ['uno_images/sonderkarten/schwarz/schwarz_plus_vier_neu.jpg', 'uno_images/sonderkarten/schwarz/schwarz_farbe_wuenschen_neu.jpg']

karten = [] # Hier werden alle Karten, die im Spiel verfügbar sind, gespeichert. Von hier werden Karten gezogen und auch wieder zurückgelegt
wunsch_farbe = ''  # Legt eine Spieler schwarz, kann er die Farbe der nächsten Karte bestimmen

# ZahlenKarten der Kartenliste zufügen
for i in range(10):
    for farbe in farben:
        if farbe == 'blau':
            karten.append(ZahlenKarte(farbe, img_blau_zahlen[i], i))
        elif farbe == 'gelb':
            karten.append(ZahlenKarte(farbe, img_gelb_zahlen[i], i))
        elif farbe == 'grün':
            karten.append(ZahlenKarte(farbe, img_gruen_zahlen[i], i))
        else:
            karten.append(ZahlenKarte(farbe, img_rot_zahlen[i], i))

# Bunte Sonderkarten der Kartenliste zufügen
for i in range(2):
    for farbe in farben:
        for wirkung in wirkungen_bunt:
            index = wirkungen_bunt.index(wirkung)
            if farbe == 'blau':
                karten.append(SonderKarte(farbe, img_wirkungen_blau[index], wirkung))
            elif farbe == 'gelb':
                karten.append(SonderKarte(farbe, img_wirkungen_gelb[index], wirkung))
            elif farbe == 'grün':
                karten.append(SonderKarte(farbe, img_wirkungen_gruen[index], wirkung))
            else:
                karten.append(SonderKarte(farbe, img_wirkungen_rot[index], wirkung))

# Schwarze Karten der Kartenliste zufügen
for i in range(4):
    for wirkung in wirkungen_schwarz:
        if wirkung == 'plus 4':
            karten.append(SonderKarte('schwarz', img_wirkungen_schwarz[0], wirkung))
        else:
            karten.append(SonderKarte('schwarz', img_wirkungen_schwarz[1], wirkung))

# erste Karte bestimmen, anpassen und aus der Karten-Liste entfernen
aktuelle_karte = random.choice(karten)
while aktuelle_karte.farbe == 'schwarz':  # Die erste Karte darf nicht schwarz sein
    aktuelle_karte = random.choice(karten) 
if isinstance(aktuelle_karte, SonderKarte):
    aktuelle_karte.genutzt = True  # Die erste Karte darf keine Wirkung haben
karten.remove(aktuelle_karte)

# Der Index für die Karte des menschlichen Spielers, die angezeigt werden soll (es wird immer nur eine Karte seines Decks auf einmal angezeigt)
mensch_karte_index = 0

##################### Spieler #############################

reihenfolge = []  # Hier werden alle Spieler-Objekte gespeichert und damit die Reihenfolge festgelegt

class Spieler:
    def __init__(self, name):
        # Erstellen des Objekts
        self.name = name
        self.deck = []  # Hier werden die Karten des Spielers gespeichert
        self.moegliche_karten = []  # Hier werden die Karten des Spielers gespeichert, die er legen könnte
        self.karte_gezogen = False  # Für den Fall, dass der Spieler eine Karte ziehen muss
        self.karten_gezogen = False  # Für den Fall, dass der Spieler mehrere Karten ziehen muss

    def reagieren(self):
        # Der Spieler ist an der Reihe und reagiert auf die aktuelle Karte
        # Zum Überprüfen, ob das Bild zur Karte passt, den Karteninhalt auf der Konsole ausgeben
        if isinstance(aktuelle_karte, SonderKarte):
            print(f'aktuelle karte = {aktuelle_karte.farbe} {aktuelle_karte.wirkung}')
        else:
            print(f'aktuelle karte = {aktuelle_karte.farbe} {aktuelle_karte.zahl}')

        self.karte_gezogen = False  # reagiert der Spieler auf die aktuelle Karte, bedeutet das auch, dass er nicht direkt davor gezogen hat
        self.karten_gezogen = False

        # Der Spieler reagiert unterschiedlich auf unterschiedliche Karten
        # ungenutzte plus 4
        if aktuelle_karte.farbe == 'schwarz' and aktuelle_karte.wirkung == 'plus 4' and aktuelle_karte.genutzt is False:
            # Der Spieler muss 4 Karten ziehen
            aktuelle_karte.genutzt = True
            self.karte_ziehen(4)
        # Farbwunschkarte, genutzte plus 4, Zahlenkarte
        elif (aktuelle_karte.farbe == 'schwarz' and aktuelle_karte.wirkung == 'Farbe wünschen') or (aktuelle_karte.farbe == 'schwarz' and aktuelle_karte.wirkung == 'plus 4' and aktuelle_karte.genutzt) or isinstance(aktuelle_karte, ZahlenKarte):
            # Der Spieler schaut, ob er eine Karte legen kann
            self.karte_suchen()
        # ungenutzte plus 2
        elif isinstance(aktuelle_karte, SonderKarte) and aktuelle_karte.wirkung == 'plus 2' and aktuelle_karte.genutzt is False:
            # Der Spieler muss 2 Karten ziehen
            aktuelle_karte.genutzt = True
            self.karte_ziehen(2)
        # ungenutzte Aussetzen
        elif isinstance(aktuelle_karte, SonderKarte) and aktuelle_karte.wirkung == 'Aussetzen' and aktuelle_karte.genutzt is False:
            # Der Spieler muss aussetzen
            aktuelle_karte.genutzt = True
            self.aussetzen()
        # der Rest (z.B. genutzte bunte Sonderkarten)
        else:
            # Der Spieler schaut, ob er eine Karte legen kann
            self.karte_suchen()

    def karte_ziehen(self, zahl):
        # Spieler zieht x Karten
        global text_1
        global text_2
        global karten
        global aktuelle_karte

        aktuelle_karte.genutzt = True

        text_1 = f'{self.name}'
        text_2 = f'muss ziehen'

        for i in range(zahl):
            karte = random.choice(karten)
            self.deck.append(karte)
            karten.remove(karte)
        
        if zahl > 1:
            self.karten_gezogen = True  # Damit der nächste Spieler nicht auch 2/4 Karten ziehen muss
        else:
            self.karte_gezogen = True  # Damit der Spieler nicht wieder zieht, wenn er immer noch nicht kann

    def aussetzen(self):
        # Der aktuelle Spieler muss aussetzen
        global text_2

        text_2 = 'muss aussetzen'

    def richtungswechsel(self):
        # Die Richung wird gewechselt
        global text_1
        global text_2
        global reihenfolge
        global aktuelle_karte

        reihenfolge.reverse()
        aktuelle_karte.genutzt = True
        
        text_1 = 'Die Richtung wird gewechselt'
        text_2 = ''

    def next(self):
        # Der nächste Spieler ist an der Reihe
        global aktueller_spieler
        global text_1
        global text_2

        index = reihenfolge.index(aktueller_spieler)
        if index == len(reihenfolge)-1: # Wenn der aktuelle Spieler der letzte in der Reihenfolge-Liste ist, ist der nächste Spieler der erste in der Reihenfolge
            aktueller_spieler = reihenfolge[0]
        else:
            aktueller_spieler = reihenfolge[index + 1]

        text_1 = f'{aktueller_spieler.name}'
        text_2 = 'ist an der Reihe'

    def karte_suchen(self):
        # Der Spieler schaut, ob er Karten hat, die er legen könnte
        global text_1
        global text_2
        self.moegliche_karten = []  # reset

        # Schwarze Karte
        if aktuelle_karte.farbe == 'schwarz':
            for eigene_karte in self.deck:
                if eigene_karte.farbe == wunsch_farbe:
                    self.moegliche_karten.append(eigene_karte)  # Passt die eigene Karte wird sie in den Mögliche-Karten-Stapel kopiert
        # Bunte Karte
        else:
            # ZahlenKarte
            if isinstance(aktuelle_karte, ZahlenKarte):
                for eigene_karte in self.deck:
                    # eigene Karte ist eine ZahlenKarte
                    if isinstance(eigene_karte, ZahlenKarte):
                        if eigene_karte.zahl == aktuelle_karte.zahl or eigene_karte.farbe == aktuelle_karte.farbe:
                            self.moegliche_karten.append(eigene_karte)
                    # eigene Karte ist eine SonderKarte
                    else:
                        if eigene_karte.farbe == aktuelle_karte.farbe or eigene_karte.farbe == 'schwarz':
                            self.moegliche_karten.append(eigene_karte)
            # Bunte SonderKarte
            else:
                for eigene_karte in self.deck:
                    if eigene_karte.farbe == aktuelle_karte.farbe or eigene_karte.farbe == 'schwarz':
                        self.moegliche_karten.append(eigene_karte)
                    elif isinstance(eigene_karte, SonderKarte):
                        if eigene_karte.wirkung == aktuelle_karte.wirkung:
                            self.moegliche_karten.append(eigene_karte)   

        print(self.moegliche_karten)  # Zur Überprüfung, ob die Logik stimmt, Ausgabe im Terminal

        text_1 = aktueller_spieler.name
        text_2 = 'sucht nach einer passenden Karte'

    def karte_waehlen(self):
        # Wenn der Spieler Karten hat, die er legen könnte, wählt er unter ihnen eine aus
        global text_2
        global gewaehlte_karte

        if self.moegliche_karten:
            gewaehlte_karte = random.choice(self.moegliche_karten)
            text_2 = 'entscheidet sich zwischen den möglichen Karten'
        else:
            text_2 = 'hat keine passende Karte'

    def karte_legen(self, karte):
        # Der Spieler legt die Karte, für die er sich entschieden hat
        global aktuelle_karte
        global karten
        global text_2
        global wunsch_farbe
        global text_3

        if isinstance(aktuelle_karte, SonderKarte) and aktuelle_karte.genutzt:
            aktuelle_karte.genutzt = False  # Damit, wenn sie wieder gezogen wird, wieder normal mit Wirkung genutzt werden kann

        wunsch_farbe = ''  # Der Wunsch wurde erfüllt
        karten.append(aktuelle_karte)  # Aktuelle Karte geht zurück in den Kartenstapel
        aktuelle_karte = karte  # Gelegte Karte wird zur aktuellen Karte
        self.deck.remove(karte)  # Aktuelle Karte wird aus dem Deck entfernt

        text_2 = 'legt eine Karte'
        text_3 = ''

    def uno(self):
        # Der Spieler hat nur noch eine Karte auf der Hand
        global text_2

        text_2 = 'hat nur noch eine Karte! UNO!'
        wow.play()

    def unouno(self):
        # Der Spieler hat keine Karteh mehr und gewinnt
        global text_1
        global text_2

        text_1 = 'Glückwunsch!'
        text_2 = f'{aktueller_spieler.name} gewinnt!'
        game_over.play()

    def farbe_wuenschen(self):
        # Der Spieler hat eine schwarze Karte gelegt und kann sich nun eine Farbe wünschen
        global wunsch_farbe
        global text_2
        global text_3

        wunsch_farbe = random.choice(farben)

        text_2 = f'wünscht {wunsch_farbe}'
        text_3 = f'Wunschfarbe: {wunsch_farbe}'

class Mensch(Spieler):
    def __init__(self, name):
        # Erstellen des Objekts
        Spieler.__init__(self, name)

        # Für Statistiken
        self.ausgesetzt = 0
        self.karten_gezogen = 0
        self.uno_anzahl = 0

    def reagieren(self):
        # Aktueller Spieler reagiert auf die aktuelle Karte
        global eigene_karte_image
        Spieler.reagieren(self)

    def karte_ziehen(self, zahl):
        # Aktueller Spieler muss x Karten ziehen
        random.choice([yikes, kill]).play()  # Soundeffekt
        Spieler.karte_ziehen(self, zahl)

        self.karten_gezogen += zahl  # Für die Statistiken

    def aussetzen(self):
        # Aktueller Spieler muss aussetzen
        Spieler.aussetzen(self)
        self.ausgesetzt += 1

    def richtungswechsel(self):
        # Die Richtung wird gewechselt
        Spieler.richtungswechsel(self)

    def next(self):
        # Der nächste Spieler ist an der Reihe
        Spieler.next(self)

    def karte_suchen(self):
        # Es wird geschaut, ob der aktuelle Spieler mindestens eine Karte legen kann
        global text_1
        global text_2
        self.moegliche_karten = []  # reset

        # Schwarze Karte
        if aktuelle_karte.farbe == 'schwarz':
            for eigene_karte in self.deck:
                if eigene_karte.farbe == wunsch_farbe:
                    self.moegliche_karten.append(eigene_karte)
        # Bunte Karte
        else:
            # ZahlenKarte
            if isinstance(aktuelle_karte, ZahlenKarte):
                for eigene_karte in self.deck:
                    # Eigene Karte ist eine ZahlenKarte
                    if isinstance(eigene_karte, ZahlenKarte):
                        if eigene_karte.zahl == aktuelle_karte.zahl or eigene_karte.farbe == aktuelle_karte.farbe:
                            self.moegliche_karten.append(eigene_karte)
                    # Eigene Karte ist eine SonderKarte
                    else:
                        if eigene_karte.farbe == aktuelle_karte.farbe or eigene_karte.farbe == 'schwarz':
                            self.moegliche_karten.append(eigene_karte)
            # Bunte SonderKarte
            else:
                for eigene_karte in self.deck:
                    if eigene_karte.farbe == aktuelle_karte.farbe or eigene_karte.farbe == 'schwarz':
                        self.moegliche_karten.append(eigene_karte)
                    elif isinstance(eigene_karte, SonderKarte):
                        if eigene_karte.wirkung == aktuelle_karte.wirkung:
                            self.moegliche_karten.append(eigene_karte)   

        print(self.moegliche_karten)  # Zur Überprüfung Ausgabe im Terminal

        text_1 = aktueller_spieler.name
        text_2 = '- hast du eine passenden Karte?'  # Unterschied zur Spielerklasse

    def karte_waehlen(self):
        # Wenn der Spieler Karten hat, die er legen könnte, muss er eine von ihnen wählen
        global text_2
        
        if self.moegliche_karten:
            text_2 = 'wählt mit den Pfeilen eine Karte'  # Mit Pfeil nach links erscheint die Karte links von der angezeigten, mit Pfeil rechts die rechte und mit Pfeil nach unten, wählt der Spieler die angezeigte Karte
        else:
            text_2 = 'hat keine passende Karte'

    def karte_legen(self, karte):
        # Der Spieler legt die Karte, für die er sich entschieden hat
        global mensch_karte_index
        
        mensch_karte_index -= 1
        Spieler.karte_legen(self, karte)
        
    def uno(self):
        # Der Spieler hat nur noch eine Karte auf der Hand
        Spieler.uno(self)
        self.uno_anzahl += 1  # Für Statistiken

    def unouno(self):
        # Der Spieler hat keine Karten mehr auf der Hand und gewinnt
        Spieler.unouno(self)

    def farbe_wuenschen(self):
        # Der Spieler hat schwarz gelegt und muss sich eine Farbe wünschen
        global text_2

        text_2 = 'muss eine Farbe wünschen'

    def farbe_eingeben(self):
        # Der Spieler muss eine Farbe eingeben
        global text_1
        global text_2

        text_1 = 'Eingeben: gelb, blau, grün, rot'
        text_2 = ''

    def farbe_gewuenscht(self):
        # Der Wunsch der Spielers wird angezeigt
        global text_2
        global text_3

        text_2 = f'wünscht {wunsch_farbe}'
        text_3 = f'Wunschfarbe: {wunsch_farbe}'

####################### Funktionen ############################

def sieben_karten_ziehen(spieler):
    # Es werden 7 random Karten aus der Karten-Liste gezogen
    # Sie werden dem Deck des jeweiligen Spielers zugefügt
    # und aus der Liste der Karten entfernt
    global karten
    for i in range(7):
        karte = random.choice(karten)
        spieler.deck.append(karte)
        karten.remove(karte)

def namen_eingeben():
    # Der Spieler wird aufgefordert, seinen Namen einzugeben
    global text_1
    global text_2
    
    text_1 = 'Gib deinen Namen ein:'
    text_2 = ''

def computergegner_waehlen():
    # Der Spieler wird aufgefordert, die Anzahl der gewünschten Computergegner anzugeben
    global text_1
    global text_2

    text_1 = 'Anzahl der gewünschten Computergegner (1-5):'
    text_2 = ''

##################### Pygame ######################

# Pygame initialisieren
pygame.init()

# Sound-Mixer initialisieren
pygame.mixer.init()

# Spielfenster zuschneiden
fenster = pygame.display.set_mode([600, 535])

# Titel im Fensterkopf
pygame.display.set_caption('UNO')

# Schriftart auswählen 
schrift = pygame.font.SysFont('Arial', 23)  # (Fontname, Größe)
schrift_klein = pygame.font.SysFont('Arial', 18)

# Textvariablen erstellen
text_1 = 'Merken:'
text_2 = 'Mit Enter geht es weiter'
text_3 = ''
text_4 = 'Aktuelle Karte'
text_5 = 'Dein Deck'
pfeil_links = '<'
pfeil_rechts = '>'
pfeil_runter = 'Karte wählen mit Pfeil runter'

# Farben auswählen
gruen = pygame.Color('green')
schwarz = pygame.Color('black')
farbe_hintergrund = gruen
farbe_schrift = schwarz

# Textfelder erstellen
text_1_fenster = pygame.Rect(0, 0, 140, 50)  # X-Position, Y-Position, Breite, Höhe
text_2_fenster = pygame.Rect(0, 53, 140, 50)
text_3_fenster = pygame.Rect(0, 490, 140, 50)
text_4_fenster = pygame.Rect(45, 98, 20, 20)
text_5_fenster = pygame.Rect(370, 98, 20, 20)
pfeil_links_fenster = pygame.Rect(280, 250, 20, 20)
pfeil_rechts_fenster = pygame.Rect(555, 250, 20, 20)
pfeil_runter_fenster = pygame.Rect(315, 490, 20, 20)

# Sounds
game_over = pygame.mixer.Sound('Movie-09.wav')
wow = pygame.mixer.Sound('Various-15.wav')
yikes = pygame.mixer.Sound('Various-16.wav')
kill = pygame.mixer.Sound('Bender-06.wav')

############################ Hauptprogramm ############################

while True:
    # Abhorchen nach Events
    for event in pygame.event.get():
        # Wenn der Spieler das Fenser schließt oder Esc drückt oder nachdem jemand gewonnen hat, Enter drückt, wird das Programm beendet
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and text_1 == 'Glückwunsch!'):
            pygame.quit()  # Deaktiviert das Pygame-Modul
            sys.exit()  # Beendet das Programm

        # Der Spieler drückt eine Taste
        elif event.type == pygame.KEYDOWN:
            
            # Rückschrittaste
            if event.key == pygame.K_BACKSPACE:  # Text löschen
                if text_1 == 'Gib deinen Namen ein:' or text_1 == 'Anzahl der gewünschten Computergegner (1-5):' or text_1 == 'Eingeben: gelb, blau, grün, rot':
                    text_2 = text_2[:-1]

            # Pfeil links
            elif event.key == pygame.K_LEFT:
                if text_2 == 'wählt mit den Pfeilen eine Karte':  # Karte links von der angezeigten darstellen
                    if mensch_karte_index == 0:  # Angezeigte Karte ist die Karte ganz links auf der Hand
                        mensch_karte_index = len(mensch.deck)-1  # dann ist die neue angezeigte Karte die ganz rechtes auf der Hand
                    elif mensch_karte_index > len(mensch.deck)-1:
                        mensch_karte_index = len(mensch.deck)-1
                    elif mensch_karte_index < 0:
                        mensch_karte_index = 0
                    else:
                        mensch_karte_index -= 1  # Ansonsten die eins weiter links

            # Pfeil rechts
            elif event.key == pygame.K_RIGHT:  # Karte rechts von der angezeigten darstellen
                if text_2 == 'wählt mit den Pfeilen eine Karte':
                    if mensch_karte_index == len(mensch.deck)-1:  # Angezeigte Karte ist die Karte ganz rechts auf der Hand
                        mensch_karte_index = 0  # dann ist die neue angezeigte Karte die ganz rechtes auf der Hand
                    elif mensch_karte_index > len(mensch.deck)-1:
                        mensch_karte_index = len(mensch.deck)-1
                    elif mensch_karte_index < 0:
                        mensch_karte_index = 0
                    else:
                        mensch_karte_index += 1  # Ansonsten die eins weiter rechts
            
            # Pfeil runter
            elif event.key == pygame.K_DOWN:
                if text_2 == 'wählt mit den Pfeilen eine Karte':  # Spieler wählt die Karte, die er legen möchte
                    if mensch.deck[mensch_karte_index] in mensch.moegliche_karten:  # Karte muss in der Liste der möglichen Karten vorhanden sein, um gelegt zu werden
                        gewaehlte_karte = mensch.deck[mensch_karte_index]
                        aktueller_spieler.karte_legen(gewaehlte_karte)
                    else:
                        aktueller_spieler.karte_waehlen()  # Ist die Karte nicht in der Liste, passiert nichts
            
            # Enter
            elif event.key == pygame.K_RETURN:  # Mit Enter bestätigt der Spieler, dass es weitergehen kann

                if text_1 == 'Merken:':
                    namen_eingeben()
                
                elif text_1 == 'Gib deinen Namen ein:':
                    try:  # Falls capitalize nicht mit der Eingabe funktioniert
                        name = text_2.strip().capitalize()
                        reihenfolge.append(Mensch(name))  # Erstellt das Objekt des menschlichen Spielers
                        text_1 = 'Anzahl der gewünschten Computergegner (1-5):'
                        text_2 = ''
                    except:
                        namen_eingeben()

                elif text_1 == 'Anzahl der gewünschten Computergegner (1-5):':
                    try:  # Falls der Spieler eine ungültige Eingabe macht
                        if int(text_2) < 1 or int(text_2) > 5:
                            computergegner_waehlen()
                        for i in range(int(text_2)):
                            reihenfolge.append(Spieler(f'Spieler {i+1}'))  # Erstellt die gewünschte Anzahl an Computergegnern
                        aktueller_spieler = random.choice(reihenfolge)  # Den ersten Spieler auslosen
                        for spieler in reihenfolge:  # Jeder Spieler bekommt zu Beginn 7 Karten
                            sieben_karten_ziehen(spieler)
                        text_1 = f'Viel Spaß, {name}'
                        text_2 = ''
                    except:
                        computergegner_waehlen()

                elif text_1 == 'Eingeben: gelb, blau, grün, rot' and text_2 == f'wünscht {wunsch_farbe}':
                    aktueller_spieler.next()

                elif text_1 == 'Eingeben: gelb, blau, grün, rot':
                    try:  # Falls der Spieler eine ungültige Eingabe macht
                        wunsch_farbe = text_2.strip().lower()
                        if wunsch_farbe in farben:  # Eingegebene Farbe muss eine gültige Farbe sein
                            aktueller_spieler.farbe_gewuenscht()
                        else:
                            aktueller_spieler.farbe_eingeben()
                    except:
                        aktueller_spieler.farbe_eingeben()

                elif text_1 == f'Viel Spaß, {name}':
                    text_1 = f'{aktueller_spieler.name} beginnt'
                    text_2 = ''
                
                elif text_1 == f'{aktueller_spieler.name} beginnt' or text_2 == 'ist an der Reihe':
                    # Der aktuelle Spieler reagiert auf die aktuelle Karte
                    aktueller_spieler.reagieren()

                elif text_2 == f'muss ziehen' and aktueller_spieler.karten_gezogen:
                    # Der Spieler schaut, ob er eine passende Karte hat
                    aktueller_spieler.karten_gezogen = False
                    aktueller_spieler.karte_suchen()

                elif text_2 == 'muss aussetzen' or text_1 == 'Die Richtung wird gewechselt' or text_2 == 'hat nur noch eine Karte! UNO!' or text_2 == f'wünscht {wunsch_farbe}':
                    # Der nächste Spieler ist ander Reihe
                    aktueller_spieler.next()

                elif text_2 == 'sucht nach einer passenden Karte' or text_2 == '- hast du eine passenden Karte?':
                    # Der Spieler wählt eine Karte
                    aktueller_spieler.karte_waehlen()
                
                elif text_2 == 'hat keine passende Karte' and aktueller_spieler.karte_gezogen is False:
                    # Der Spieler muss 1/2/4 Karten ziehen
                    aktueller_spieler.karte_ziehen(1)
                
                elif text_2 == 'hat keine passende Karte' and aktueller_spieler.karte_gezogen:
                    # Der nächste Spieler ist an der Reihe
                    aktueller_spieler.karte_gezogen = False
                    aktueller_spieler.next()

                elif text_2 == f'muss ziehen':
                    # Dopplung? Wenn ichs entferne, gehts Spiel nicht mehr
                    aktueller_spieler.karte_suchen()

                elif text_2 == 'entscheidet sich zwischen den möglichen Karten':
                    # Der Spieler muss eine Karte legen
                    if aktueller_spieler.karte_gezogen:
                        aktueller_spieler.karte_gezogen = False  # Da es mögliche Karten gibt, muss er ab jetzt wieder in der Lage sein, Karten zu ziehen
                    aktueller_spieler.karte_legen(gewaehlte_karte)

                elif text_2 == 'legt eine Karte' and len(aktueller_spieler.deck) == 0:
                    # Der Spieler hat keine Karte mehr auf der Hand
                    aktueller_spieler.unouno()

                elif text_2 == 'legt eine Karte' and aktuelle_karte.farbe == 'schwarz' and wunsch_farbe == '':
                    # Der Spieler muss sich eine Farbe wünschen
                    aktueller_spieler.farbe_wuenschen()
                
                elif text_2 == 'legt eine Karte' and len(aktueller_spieler.deck) == 1:
                    # Der Spieler hat nur noch eine Karte auf der Hand
                    aktueller_spieler.uno()

                elif text_2 == 'muss eine Farbe wünschen':
                    # Der Spieler muss eine Farbe eingeben
                    aktueller_spieler.farbe_eingeben()

                elif text_2 == 'legt eine Karte' and isinstance(aktuelle_karte, SonderKarte) and aktuelle_karte.wirkung == 'Richtungswechsel' and aktuelle_karte.genutzt is False:
                    # Die Richtung wird gewechselt
                    aktueller_spieler.richtungswechsel()

                elif text_2 == 'legt eine Karte':
                    # Der nächste Spieler ist an der Reihe
                    aktueller_spieler.next()

                elif text_1 == 'Die Richtung wird gewechselt':
                    # Der nächste Spieler ist an der Reihe
                    aktueller_spieler.next()

                elif text_2 == f'wünscht {wunsch_farbe}':
                    # Der nächste Spieler ist an der Reihe
                    if len(aktueller_spieler.deck) == 1:
                        aktueller_spieler.uno()
                        
                    elif len(aktueller_spieler.deck) == 0:
                        aktueller_spieler.unouno()
                    aktueller_spieler.next()

            # Andere Tasten als Esc, Pfeile, Backspace oder Enter
            else:
                if text_1 == 'Gib deinen Namen ein:' or text_1 == 'Anzahl der gewünschten Computergegner (1-5):' or text_1 == 'Eingeben: gelb, blau, grün, rot':
                    text_2 += event.unicode  # Schreiben 

    # Hintergrundsfarbe
    fenster.fill(gruen)

    # Text-Fenster darstellen
    # Text 1
    pygame.draw.rect(fenster, farbe_hintergrund, text_1_fenster)  # Text-Fenster erstellen
    text_oberflaeche_1 = schrift.render(text_1, True, farbe_schrift)  # Inhalt einfügen
    fenster.blit(text_oberflaeche_1, (text_1_fenster.x+5, text_1_fenster.y+10))  # Positionieren
    text_1_fenster.w = max(100, text_oberflaeche_1.get_width()+10)  # Breite des Text-Fensters dem Inhalt anpassen

    # Text 2
    pygame.draw.rect(fenster, farbe_hintergrund, text_2_fenster)
    text_oberflaeche_2 = schrift.render(text_2, True, farbe_schrift)
    fenster.blit(text_oberflaeche_2, (text_2_fenster.x+5, text_2_fenster.y+10))
    text_2_fenster.w = max(100, text_oberflaeche_2.get_width()+10)

    # Text 3 (Wunschfarbe)
    pygame.draw.rect(fenster, farbe_hintergrund, text_3_fenster)
    text_oberflaeche_3 = schrift.render(text_3, True, farbe_schrift)
    fenster.blit(text_oberflaeche_3, (text_3_fenster.x+5, text_3_fenster.y+10))
    text_3_fenster.w = max(100, text_oberflaeche_3.get_width()+10)

    # Text 4 (Aktuelle Karte)
    pygame.draw.rect(fenster, farbe_hintergrund, text_4_fenster)
    text_oberflaeche_4 = schrift_klein.render(text_4, True, farbe_schrift)
    fenster.blit(text_oberflaeche_4, (text_4_fenster.x+5, text_4_fenster.y+10))

    # Text 5 (Dein Deck)
    pygame.draw.rect(fenster, farbe_hintergrund, text_5_fenster)
    text_oberflaeche_5 = schrift_klein.render(text_5, True, farbe_schrift)
    fenster.blit(text_oberflaeche_5, (text_5_fenster.x+5, text_5_fenster.y+10))

    # Pfeil links
    pygame.draw.rect(fenster, gruen, pfeil_links_fenster)
    pfeil_links_oberflaeche = schrift.render(pfeil_links, True, farbe_schrift)
    fenster.blit(pfeil_links_oberflaeche, (pfeil_links_fenster.x, pfeil_links_fenster.y))

    # Pfeil rechts
    pygame.draw.rect(fenster, gruen, pfeil_rechts_fenster)
    pfeil_rechts_oberflaeche = schrift.render(pfeil_rechts, True, farbe_schrift)
    fenster.blit(pfeil_rechts_oberflaeche, (pfeil_rechts_fenster.x, pfeil_rechts_fenster.y))

    # Pfeil runter
    pygame.draw.rect(fenster, gruen, pfeil_runter_fenster)
    pfeil_runter_oberflaeche = schrift_klein.render(pfeil_runter, True, farbe_schrift)
    fenster.blit(pfeil_runter_oberflaeche, (pfeil_runter_fenster.x, pfeil_runter_fenster.y))
   
    # Bilder darstellen
    # Aktuelle Karte
    aktuelle_karte_image = pygame.image.load(f'{aktuelle_karte.image}')
    fenster.blit(aktuelle_karte_image, (10, 130))  # (X-Position, Y-Position)

    # Deck
    if text_1 == 'Merken:' or text_1 == 'Gib deinen Namen ein:' or text_1 == 'Anzahl der gewünschten Computergegner (1-5):':
        eigene_karte_image = pygame.image.load('uno_images/blank_neu.jpg')  # Wenn es noch keine Spielerobjekte gibt, wird eine weiße Karte angezeigt
    else:
        for spieler in reihenfolge:
            if isinstance(spieler, Mensch):
                mensch = spieler
        if len(mensch.deck) == 0:  # Wenn der menschliche Spieler seine letzte Karte gelegt hat, wird eine weiße Karte angezeigt
            eigene_karte_image = pygame.image.load('uno_images/blank_neu.jpg')
        else:
            eigene_karte_image = pygame.image.load(mensch.deck[mensch_karte_index].image)  # Ansonsten wird eine Karte aus dem Deck des menschlichen Spielers angezeigt
    
    fenster.blit(eigene_karte_image, (320, 130))

    # Updaten des Fensters
    pygame.display.flip()  # updatet das Spielfenster