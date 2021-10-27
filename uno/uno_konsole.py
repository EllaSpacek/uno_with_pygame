# UNO-Konsolen-Spiel
# Anmerkung: Dies ist ein erster Versuch, um zu sehen, ob die Logik dahinter passt.
# Diese Version ist nicht ausreichend getestet worden und unterscheidet sich mit ihren Funktionen in einigen Punkten von der Pygame-Variante

import time
import random

####################### Klassen ###########################

####################### Karten ############################

class Karte:
    # hiervon erben alle anderen Karten
    # alle Arten von Karten haben eine Gemeinsamkeit: sie haben alle eine Farbe
    def __init__(self, farbe, image):
        self.farbe = farbe
        self.image = image


class ZahlenKarte(Karte):
    # ZahlenKarten sind bunte Karten mit Zahlen
    def __init__(self, farbe, image, zahl):
        super().__init__(farbe, image)
        self.zahl = zahl


class SonderKarte(Karte):
    # Sonderkarten sind Karten ohne Zahlen
    def __init__(self, farbe, image, auswirkung):
        super().__init__(farbe, image)
        self.auswirkung = auswirkung
        self.genutzt = False

####################### Spieler #############################

class Spieler:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.moegliche_karten = []

    def reagieren(self):
        print(f'{self.name} ist an der Reihe.')
        # Zahlenkarte
        if isinstance(aktuelle_karte, ZahlenKarte):
            print(f'Die aktuelle Karte ist {aktuelle_karte.farbe}, {aktuelle_karte.zahl}.')
            # Überprüfen, ob passende Karte vorhanden
            self.karte_suchen()
        # Sonderkarte
        else:
            print(f'Die aktuelle Karte ist {aktuelle_karte.farbe}, {aktuelle_karte.auswirkung}.')
            if aktuelle_karte.farbe == 'schwarz':
                # Schwarze Karte
                if aktuelle_karte.auswirkung == 'plus 4' and aktuelle_karte.genutzt is False:
                    # Der Spieler muss 4 Karten ziehen
                    print(f'{self.name} muss 4 karten ziehen.')
                    aktuelle_karte.genutzt = True
                    for i in range(4):
                        self.karte_ziehen()
                    # Überprüfen, ob passende Karte vorhanden
                    self.karte_suchen()
                elif (aktuelle_karte.auswirkung == 'plus 4' and aktuelle_karte.genutzt) or aktuelle_karte.auswirkung == 'Farbe wünschen':
                    # Der Spieler muss KEINE 4 Karten ziehen
                    # Überprüfen, ob passende Karte vorhanden
                    self.karte_suchen()
            else:
                # Bunte Karte
                # Zahlenkarte
                if isinstance(aktuelle_karte, ZahlenKarte):
                    # Überprüfen, ob passende Karte vorhanden
                    self.karte_suchen()
                else:
                    # Sonderkarte
                    # Plus 2 neu
                    if aktuelle_karte.auswirkung == 'plus 2' and aktuelle_karte.genutzt is False:
                        print(f'{self.name} muss 2 Karten ziehen.')
                        aktuelle_karte.genutzt = True
                        for i in range(2):
                            self.karte_ziehen()
                        # Überprüfen, ob passende Karte vorhanden
                        self.karte_suchen()
                    # Aussetzen neu
                    elif aktuelle_karte.auswirkung == 'Aussetzen' and aktuelle_karte.genutzt is False:
                        print(f'{self.name} muss eine Runde aussetzen.')
                        aktuelle_karte.genutzt = True
                    # Sonderkarten alt
                    elif aktuelle_karte.genutzt is True:
                        self.karte_suchen()

        # Der nächste Spieler ist an der Reihe
        self.next()

    def karte_ziehen(self):
        # Karte wird aus der Kartenliste gezogen und dem eigenen Deck beigefügt
        global karten

        karte = random.choice(karten)
        self.deck.append(karte)
        karten.remove(karte)

    def karte_suchen(self):
        self.moegliche_karten = []
        # Farbe überprüfen
        # Schwarze Karte
        if aktuelle_karte.farbe == 'schwarz':
            for eigene_karte in self.deck:
                if eigene_karte.farbe == wunsch_farbe:
                    # Falls Karte vorhanden, wird sie der Liste der möglichen Karten beigefügt
                    self.moegliche_karten.append(eigene_karte)
        # Bunte Karte
        else:
            # Zahlenkarte
            if isinstance(aktuelle_karte, ZahlenKarte):
                for eigene_karte in self.deck:
                    # eigene Karte ist eine Zahlenkarte
                    if isinstance(eigene_karte, ZahlenKarte):
                        if eigene_karte.zahl == aktuelle_karte.zahl or eigene_karte.farbe == aktuelle_karte.farbe:
                            # Falls Karte vorhanden, wird sie der Liste der möglichen Karten beigefügt
                            self.moegliche_karten.append(eigene_karte)
                    # eigene Karte ist eine bunte Sonderkarte
                    else:
                        if eigene_karte.farbe == aktuelle_karte.farbe or eigene_karte.farbe == 'schwarz':
                            # Falls Karte vorhanden, wird sie der Liste der möglichen Karten beigefügt
                            self.moegliche_karten.append(eigene_karte)
            # Bunte Sonderkarte
            else:
                # Plus 2
                if aktuelle_karte.auswirkung == 'plus 2' and aktuelle_karte.genutzt is False:
                    print(f'{self.name} muss 2 Karten ziehen')
                    self.karte_ziehen()
                    self.karte_ziehen()
                    # Auswirkung der Karte wurde genutzt -> Attribut genutzt wird auf True gesetzt
                    aktuelle_karte.genutzt = True
                    for eigene_karte in self.deck:
                        if eigene_karte.farbe == aktuelle_karte.farbe or eigene_karte.farbe == 'schwarz':
                            # Falls Karte vorhanden, wird sie der Liste der möglichen Karten beigefügt
                            self.moegliche_karten.append(eigene_karte)
                        elif isinstance(eigene_karte, SonderKarte):
                            if eigene_karte.auswirkung == aktuelle_karte.auswirkung:
                                # Falls Karte vorhanden, wird sie der Liste der möglichen Karten beigefügt
                                self.moegliche_karten.append(eigene_karte)
                # Aussetzen oder Richtungswechsel
                else:
                    for eigene_karte in self.deck:
                        if eigene_karte.farbe == aktuelle_karte.farbe or eigene_karte.farbe == 'schwarz':
                            # Falls Karte vorhanden, wird sie der Liste der möglichen Karten beigefügt
                            self.moegliche_karten.append(eigene_karte)
                        elif isinstance(eigene_karte, SonderKarte):
                            if eigene_karte.auswirkung == aktuelle_karte.auswirkung:
                                # Falls Karte vorhanden, wird sie der Liste der möglichen Karten beigefügt
                                self.moegliche_karten.append(eigene_karte)
        self.karte_waehlen()    

    def karte_waehlen(self):
        # Wenn mindestens eine mögliche Karten vorhanden ist
        if self.moegliche_karten:
            geawehlte_karte = random.choice(self.moegliche_karten)
            self.karte_legen(geawehlte_karte)  
        # Falls keine passende Karte vorhanden, noch eine ziehen, nicht legen
        else:
            print(f'{self.name} hat keine geeignete Karte und muss eine ziehen.')
            self.karte_ziehen()

    def karte_legen(self, karte):
        global aktuelle_karte
        global karten

        # Akuelle Karte geht zurück in die Karten-Liste
        karten.append(aktuelle_karte)
        # Gelegte Karte wird zur aktuellen Karte
        aktuelle_karte = karte
        # Gelegte Karte wird aus eigenem Deck entfernt
        self.deck.remove(karte)

        if not self.deck:
            print(f'''UNO-UNO!!!!!
Glückwunsch {self.name}, gewinnt.''')
            print()
            rangliste()
        elif len(self.deck) == 1:
            print(f'''UNO!!!!
Hat nur noch eine Karte auf der Hand!''')

        # Farbe wünschen
        if aktuelle_karte.farbe == 'schwarz':
            self.farbe_wuenschen()

    def farbe_wuenschen(self):
        global wunsch_farbe
        wunsch_farbe = random.choice(farben)
        print(f'{self.name} wählt die Farbe {wunsch_farbe}.')

    def next(self):
        # Der nächste Spieler kommt an die Reihe
        global reihenfolge
        global aktueller_spieler
        global aktuelle_karte
    
        # Richtungswechsel
        if isinstance(aktuelle_karte, SonderKarte):
            if aktuelle_karte.auswirkung == 'Richtungswechsel' and aktuelle_karte.genutzt is False:
                print('Die Richtung wird gewechselt.')
                reihenfolge.reverse()
                aktuelle_karte.genutzt = True
        index = reihenfolge.index(aktueller_spieler)
        if index == len(reihenfolge)-1:
        # Wenn der bisherige aktuelle Spieler der letzte in der Liste Reihenfolge ist, ist der nächste Spieler der erste Spieler der Liste
            aktueller_spieler = reihenfolge[0]
        else:
            aktueller_spieler = reihenfolge[index + 1]

######################### Menschlicher Spieler #########################

class Mensch(Spieler):
    def __init__(self, name):
        # Erstellt Name und Deck
        Spieler.__init__(self, name)

        # Für Statistiken
        self.ausgesetzt = 0
        self.karten_gezogen = 0
        self.uno = 0

    def reagieren(self):
        print(f'{self.name} ist an der Reihe.')
        # Zahlenkarte
        if isinstance(aktuelle_karte, ZahlenKarte):
            print(f'Die aktuelle Karte ist {aktuelle_karte.farbe}, {aktuelle_karte.zahl}.')
            # Überprüfen, ob passende Karte vorhanden
            self.karte_suchen()
        # Sonderkarte
        else:
            print(f'Die aktuelle Karte ist {aktuelle_karte.farbe}, {aktuelle_karte.auswirkung}.')
            if aktuelle_karte.farbe == 'schwarz':
                # Schwarze Karte
                if aktuelle_karte.auswirkung == 'plus 4' and aktuelle_karte.genutzt is False:
                    # Der Spieler muss 4 Karten ziehen
                    print(f'{self.name} muss 4 karten ziehen.')
                    aktuelle_karte.genutzt = True
                    for i in range(4):
                        self.karte_ziehen()
                    # Überprüfen, ob passende Karte vorhanden
                    self.karte_suchen()
                elif (aktuelle_karte.auswirkung == 'plus 4' and aktuelle_karte.genutzt) or aktuelle_karte.auswirkung == 'Farbe wünschen':
                    # Der Spieler muss KEINE 4 Karten ziehen
                    # Überprüfen, ob passende Karte vorhanden
                    self.karte_suchen()
            else:
                # Bunte Karte
                # Zahlenkarte
                if isinstance(aktuelle_karte, ZahlenKarte):
                    # Überprüfen, ob passende Karte vorhanden
                    self.karte_suchen()
                else:
                    # Sonderkarte
                    # Plus 2 neu
                    if aktuelle_karte.auswirkung == 'plus 2' and aktuelle_karte.genutzt is False:
                        print(f'{self.name} muss 2 Karten ziehen.')
                        aktuelle_karte.genutzt = True
                        for i in range(2):
                            self.karte_ziehen()
                        # Überprüfen, ob passende Karte vorhanden
                        self.karte_suchen()
                    # Aussetzen neu
                    elif aktuelle_karte.auswirkung == 'Aussetzen' and aktuelle_karte.genutzt is False:
                        print(f'{self.name} muss eine Runde aussetzen.')
                        self.ausgesetzt += 1 # Hier unterscheidet sich der Mensch vom Computer
                        aktuelle_karte.genutzt = True
                    # Sonderkarten alt
                    elif aktuelle_karte.genutzt is True:
                        self.karte_suchen()
        # Der nächste Spieler ist an der Reihe
        self.next()

    def karte_ziehen(self):
        Spieler.karte_ziehen(self)

        # Für Statistiken
        self.karten_gezogen += 1

    def karte_suchen(self):
        Spieler.karte_suchen(self)

    def karte_waehlen(self):
        # Eine Karte aus der Liste der möglichen Karten auswählen
        # Anzeige aller Karten im Deck (kann Wahl der zu legenden Karte beeiflussen)
        print('Hier ein Überblick über dein Deck:')
        for karte in self.deck:
            if isinstance(karte, SonderKarte):
                print(f'Farbe: {karte.farbe}, Auswirkung: {karte.auswirkung}')
            else:
                print(f'Farbe: {karte.farbe}, Zahl: {karte.zahl}')
        # Wenn es in der Liste der möglichen Karten, mindestens eine Karte gibt
        if self.moegliche_karten:
            print(f'''{self.name}, du kannst folgende Karte(n) legen -
bitte wähle mit der vorangestellten Zahl, welche Karte du nehmen möchtest:''')
            for karte in self.moegliche_karten:
                # Anzeige der möglichen Karten
                index = self.moegliche_karten.index(karte)
                if isinstance(karte, SonderKarte):
                    print(f'{index+1} - Farbe: {karte.farbe}, Auswirkung: {karte.auswirkung}')
                else:
                    print(f'{index+1} - Farbe: {karte.farbe}, Zahl: {karte.zahl}')
            try:
                # Auswahl einer Karte
                wahl = int(input(f'''Wähle nun.
>>> ''').strip())
                self.karte_legen(self.moegliche_karten[wahl-1])
            except:
                # Der Spieler hat eine ungültige Eingabe gemacht
                print('Ungültige Eingabe.')
                self.karte_waehlen()
        # Es gibt keine passenden Karten
        else:
            print(f'''{self.name}, du hast leider keine passenden Karten.
Ziehe eine weitere, danach ist der nächste Spieler an der Reihe.''')
            print('Du ziehst eine Karte.')
            self.karte_ziehen()

    def karte_legen(self, karte):
        global aktuelle_karte
        global karten

        # Akuelle Karte geht zurück in die Karten-Liste
        karten.append(aktuelle_karte)
        # Gelegte Karte wird zur aktuellen Karte
        aktuelle_karte = karte
        # Gelegte Karte wird aus eigenem Deck entfernt
        self.deck.remove(karte)

        if not self.deck:
            print(f'''UNO-UNO!!!!!
Glückwunsch, {self.name} gewinnt.''')
            print()
            rangliste()
        elif len(self.deck) == 1:
            print(f'''UNO!!!!
{self.name} hat nur noch eine Karte auf der Hand!''')
            self.uno += 1  # Hier unterscheidet sich der Mensch vom Computer

        # Farbe wünschen
        if aktuelle_karte.farbe == 'schwarz':
            self.farbe_wuenschen()

    def farbe_wuenschen(self):
        global wunsch_farbe
        print('Wähle eine Farbe:')
        for farbe in farben:
            print(farbe)
        gewaehlte_farbe = input('>>> ').strip().lower()
        if gewaehlte_farbe in farben:
            wunsch_farbe = gewaehlte_farbe
        else:
            print('Ungültige Eingabe.')
            self.farbe_wuenschen()

    def next(self):
        Spieler.next(self)

#################### Computer Spieler ##########################

class Computer(Spieler):
    def __init__(self, name):
        # Erstellt Name und Deck
        Spieler.__init__(self, name)

    def ragieren(self):
        Spieler.reagieren(self)

    def karte_ziehen(self):
        Spieler.karte_ziehen(self)

    def karte_suchen(self):
        print(f'{self.name} schaut nach einer geeigneten Karte.')
        time.sleep(1.5)

        Spieler.karte_suchen(self)

    def karte_waehlen(self):
        Spieler.karte_waehlen(self)

    def karte_legen(self, karte):
        print(f'{self.name} legt eine Karte.')

        Spieler.karte_legen(self, karte)

    def farbe_wuenschen(self):
        Spieler.farbe_wuenschen(self)

    def next(self):
        Spieler.next(self)


################# Funktionen ##############################

def anzahlSpieler():
    # Der User-Spieler wird aufgefordert, anzugeben, gegen wie viele NPCs er spielen will
    try:
        npc = int(input('''Bitte gebe an, gegen wie viele Computergegner du spielen möchtest.
>>> '''))
        if npc > 0:
            return npc
        else:
            raise Exception()
    except:
        anzahlSpieler()

def sieben_karten_ziehen(spieler):
    # Es werden 7 random Karten aus der Karten-Liste gezogen, dem Deck des Spielers beigefügt und aus der Karten-Liste entfernt
    global karten
    for i in range(7):
        karte = random.choice(karten)
        spieler.deck.append(karte)
        karten.remove(karte)

def rangliste():
    # Gibt die Punktzahl der einzelnen Spieler aus
    punkte = {}
    for spieler in reihenfolge:
        counter = 0
        for karte in spieler.deck:
            if isinstance(karte, ZahlenKarte):
                counter += karte.zahl
            elif karte.auswirkung == 'plus 2':
                counter += 20
            elif karte.auswirkung == 'Aussetzen':
                counter += 20
            elif karte.auswirkung == 'Richtungswechsel':
                counter += 20
            elif karte.auswirkung == 'Farbe wünschen':
                counter += 50
            else:
                counter += 70
        punkte[spieler.name] = counter
    
    print('Überblick über die Punkte (nicht vergessen - je weniger Punkte, desto besser):')
    for spieler, punktzahl in punkte.items():
        print(f'{spieler} hat {punktzahl} Punkte.')

    # Spieler-Statistiken ausgeben
    for spieler in reihenfolge:
        if isinstance(spieler, Mensch):
            print()
            print(f'''Überblick über deine Statistiken:
Du hast {spieler.karten_gezogen} Mal ziehen müssen.
Du hast {spieler.ausgesetzt} Mal aussetzen müssen.
Und du hast {spieler.uno} Mal fast gewonnen.''')
    # Spieler kann noch einmal spielen oder das Spiel beenden
    nochmal()
        

def vorbereiten():
    global karten
    global farben
    global wunsch_farbe
    global reihenfolge
    global aktuelle_karte
    global aktueller_spieler 

    farben = ['blau', 'gelb', 'grün', 'rot']
    img_blau_zahlen = ['uno_images/zahlenkarten/blau/blau_null.PNG', 'uno_images/zahlenkarten/blau/blau_eins.PNG', 'uno_images/zahlenkarten/blau/blau_zwei.PNG', 'uno_images/zahlenkarten/blau/blau_drei.PNG', 'uno_images/zahlenkarten/blau/blau_vier.PNG', 'uno_images/zahlenkarten/blau/blau_fuenf.PNG', 'uno_images/zahlenkarten/blau/blau_sechs.PNG', 'uno_images/zahlenkarten/blau/blau_sieben.PNG', 'uno_images/zahlenkarten/blau/blau_acht.PNG', 'uno_images/zahlenkarten/blau/blau_neun.PNG']
    img_gelb_zahlen = ['uno_images/zahlenkarten/gelb/gelb_null.PNG', 'uno_images/zahlenkarten/gelb/gelb_eins.PNG', 'uno_images/zahlenkarten/gelb/gelb_zwei.PNG', 'uno_images/zahlenkarten/gelb/gelb_drei.PNG', 'uno_images/zahlenkarten/gelb/gelb_vier.PNG', 'uno_images/zahlenkarten/gelb/gelb_fuenf.PNG', 'uno_images/zahlenkarten/gelb/gelb_sechs.PNG', 'uno_images/zahlenkarten/gelb/gelb_sieben.PNG', 'uno_images/zahlenkarten/gelb/gelb_acht.PNG', 'uno_images/zahlenkarten/gelb/gelb_neun.PNG']
    img_gruen_zahlen = ['uno_images/zahlenkarten/gruen/gruen_null.PNG', 'uno_images/zahlenkarten/gruen/gruen_eins.PNG', 'uno_images/zahlenkarten/gruen/gruen_zwei.PNG', 'uno_images/zahlenkarten/gruen/gruen_drei.PNG', 'uno_images/zahlenkarten/gruen/gruen_vier.PNG', 'uno_images/zahlenkarten/gruen/gruen_fuenf.PNG', 'uno_images/zahlenkarten/gruen/gruen_sechs.PNG', 'uno_images/zahlenkarten/gruen/gruen_sieben.PNG', 'uno_images/zahlenkarten/gruen/gruen_acht.PNG', 'uno_images/zahlenkarten/gruen/gruen_neun.PNG']
    img_rot_zahlen = ['uno_images/zahlenkarten/rot/rot_null.PNG', 'uno_images/zahlenkarten/rot/rot_eins.PNG', 'uno_images/zahlenkarten/rot/rot_zwei.PNG', 'uno_images/zahlenkarten/rot/rot_drei.PNG', 'uno_images/zahlenkarten/rot/rotn_vier.PNG', 'uno_images/zahlenkarten/rot/rot_fuenf.PNG', 'uno_images/zahlenkarten/rot/rot_sechs.PNG', 'uno_images/zahlenkarten/rot/rot_sieben.PNG', 'uno_images/zahlenkarten/rot/rot_acht.PNG', 'uno_images/zahlenkarten/rot/rot_neun.PNG']
    auswirkungen_bunt = ['plus 2', 'Richtungswechsel', 'Aussetzen']
    img_auswirkungen_blau = ['uno_images/sonderkarten/farben/blau_plus_zwei', 'uno_images/sonderkarten/farben/blau_richtungswechsel', 'uno_images/sonderkarten/farben/blau_aussetzen']
    img_auswirkungen_gelb = ['uno_images/sonderkarten/farben/gelb_plus_zwei', 'uno_images/sonderkarten/farben/gelb_richtungswechsel', 'uno_images/sonderkarten/farben/gelb_aussetzen']
    img_auswirkungen_gruen = ['uno_images/sonderkarten/farben/gruen_plus_zwei', 'uno_images/sonderkarten/farben/gruen_richtungswechsel', 'uno_images/sonderkarten/farben/gruen_aussetzen']
    img_auswirkungen_rot = ['uno_images/sonderkarten/farben/rot_plus_zwei', 'uno_images/sonderkarten/farben/rot_richtungswechsel','uno_images/sonderkarten/farben/rot_aussetzen']
    auswirkungen_schwarz = ['plus 4', 'Farbe wünschen']
    img_auswirkungen_schwarz = ['uno_images/sonderkarten/schwarz_plus_vier', 'uno_images/sonderkarten/schwarz_farbe_wuenschen']
    wunsch_farbe = ''
    reihenfolge = []

    # Spielkarten, die im Spiel verfügbar sind, generieren
    karten = []

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

    for i in range(4):
        for farbe in farben:
            for wirkung in auswirkungen_bunt:
                index = auswirkungen_bunt.index(wirkung)
                if farbe == 'blau':
                    karten.append(SonderKarte(farbe, img_auswirkungen_blau[index], wirkung))
                elif farbe == 'gelb':
                    karten.append(SonderKarte(farbe, img_auswirkungen_gelb[index], wirkung))
                elif farbe == 'gruen':
                    karten.append(SonderKarte(farbe, img_auswirkungen_gruen[index], wirkung))
                else:
                    karten.append(SonderKarte(farbe, img_auswirkungen_rot[index], wirkung))

    for i in range(4):
        for wirkung in auswirkungen_schwarz:
            if wirkung == 'plus 4': 
                karten.append(SonderKarte('schwarz', img_auswirkungen_schwarz[0], wirkung))
            else:
                karten.append(SonderKarte('schwarz', img_auswirkungen_schwarz[1], wirkung))

    # erste Karte erstellen:
    aktuelle_karte = random.choice(karten)

    # die erste Karte darf nicht schwarz sein
    while aktuelle_karte.farbe == 'schwarz':
        aktuelle_karte = random.choice(karten)

    # Die erste aktuelle Karte hat keine Auswirkungen
    if isinstance(aktuelle_karte, SonderKarte):
        aktuelle_karte.genutzt = True

    # erste Karte von der Liste der verfügbaren Karten entfernen
    karten.remove(aktuelle_karte)

    spieler_name = input('''Bitte gebe deinen Namen an.
>>> ''').strip().capitalize()
    reihenfolge.append(Mensch(spieler_name))

    # Spieler erstellen
    npc = anzahlSpieler()

    for i in range(npc):
        reihenfolge.append(Computer(f'Spieler {i+1}'))

    ########## Karten ausgeben und den ersten Spieler auslosen #############

    # jeder Spieler bekommt zu Beginn 7 Karten
    for spieler in reihenfolge:
        sieben_karten_ziehen(spieler)

    # den ersten Spieler auslosen
    aktueller_spieler = random.choice(reihenfolge)

    ######################## Spiel-Beginn #####################

    print(f'Es spielen:')
    for spieler in reihenfolge:
        print(spieler.name)

    # Prüfen, ob ein NPC oder der User-Spieler beginnt
    if isinstance(aktueller_spieler, Spieler):
        print(f'Du, {aktueller_spieler.name}, beginnst.')
    else:
        print(f'{aktueller_spieler.name} beginnt.')

    # Solange der Spieler, der an der Reihe ist, noch Karten in seinem Deck hat, läuft das Spiel
    while aktueller_spieler.deck:
        aktueller_spieler.reagieren()

def nochmal():
    print()
    weiter = input('''Möchtest du noch einmal spielen (S) oder reicht es dir (E)?
>>>''').strip().upper()
    if weiter == 'S':
        vorbereiten()
    elif weiter == 'E':
        quit()
    else:
        nochmal()


############### Spiel beginnen #####################

vorbereiten()