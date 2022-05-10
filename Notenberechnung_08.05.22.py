# Einheit 2 - Notenberechnung
# 08.05.2022, Christian Thomas

from pydoc import Helper
from re import A

print ("\n Hallo! Dieses Programm berechnet, welche Gesamtnotenstufe Sie für die Erste Juristische Staatsprüfung, die Erste Juristische Universitätsprüfung und die Erste Juristische Prüfung erzielt haben. \n")

## Variablen
# Staatsprüfung
schriftliche_staatsprüfung = []
schriftliche_staatsprüfung_gesamt = 0

mündliche_staatsprüfung = []
mündliche_staatsprüfung_gesamt = 0

staatsprüfung_gesamt = 0

# Uniprüfung
seminar = []
seminar_gesamt = 0

uni_prüfung = []
uni_prüfung_gesamt = 0

uni_prüfung_verrechnet = 0


endnote = 0

# Hilfsvariable
referenz = 0





## Funktionen

# Eingabe Prüfungen
def eingabe_prüfungen(anzahl_prüfungen, art_der_prüfung):  
 zähler = 0
 while anzahl_prüfungen > len (art_der_prüfung):
     try :
        zähler += 1
        zwischenvar = int (input (f"Geben sie die Note für Prüfung {0+ zähler} ein: "))
        art_der_prüfung.append(zwischenvar)
     except ValueError:
        print ("Geben Sie nur ganze Zahlen ein.")
        zähler -= 1


# Berechnung Gesamtnote
def berechnung_gesamtnote(art_der_prüfung, gesamtnote):
    for i in range (len (art_der_prüfung)):
        gesamtnote += art_der_prüfung [0 + i]
    gesamtnote = float (gesamtnote / len(art_der_prüfung))
    return gesamtnote

# Verrechnung Gesamtnoten
def verrechnung(note_a, note_b, anteil):
    verrechnung = (note_a * anteil) + (note_b * (1-anteil))
    return verrechnung

# Durchgefallen ?
def durchgefallen(punkte, namePrüfung, liste, schwelle):
    liste.sort()
    if (liste[0] < 4) and (liste [1] < 4) and (liste [2] < 4):
        print("Sie haben in mindestens drei Ihrer Prüfungen weniger als 4 Punkte erhalten und sind deshalb durchgefallen.")
        exit()
    elif (punkte) >= schwelle :
        print(f"Sie haben die {namePrüfung} mit {punkte} Punkten bestanden. \n")
    
    else :
        print(f"Sie sind mit {punkte} Punkten durch die {namePrüfung} gefallen und haben die Erste Juristische Prüfung somit insgesamt nicht bestanden.")
        notenstufe (punkte)
        exit()
    
    if referenz == 333:
        print("Damit haben Sie insgesamt bestanden. \n")

# Notenstufe
def notenstufe(punktezwei):
 if (punktezwei) <= 1.49:
        print ("Note in Worten: 'ungenügend'")
 elif (punktezwei) <= 3.99:
        print ("Note in Worten: 'mangelhaft'")
 elif (punktezwei) <= 6.49:
        print ("Note in Worten: 'ausreichend'")
 elif (punktezwei) <= 8.99:
        print ("Note in Worten: 'befriedigend'")
 elif (punktezwei) <= 11.49:
        print ("Note in Worten: 'vollbefriedigend'")
 elif (punktezwei) <= 13.99:
        print ("Note in Worten: 'gut'")
 elif (punktezwei) <= 18:
        print ("Note in Worten: 'sehr gut'")







## Eingabe Staatsprüfung
# Eingabe Anzahl Prüfungen
while True:
    try:
        anzahl_schrift_staat = int (input ("Wie viele schriftliche Prüfungen hatten Sie für die Staatsprüfung (max. 6) " )) 
        if anzahl_schrift_staat > 6:
            print ("Sie können maximal sechs Prüfungen absolviert haben.")
        else:
             break
    except ValueError:
        print ("Bitte geben Sie nur ganze Zahlen ein.")

# Eingabe Noten schriftliche Staatsprüfung
print ("\n Geben Sie bitte nun die Noten der schriftlichen Staatsprüfungen ein.")
eingabe_prüfungen (anzahl_schrift_staat, schriftliche_staatsprüfung)

# Eingabe Noten mündliche Staatsprüfung
print("\n Geben Sie bitte nun die Noten der drei mündlichen Staatsprüfungen ein.")
eingabe_prüfungen (3, mündliche_staatsprüfung)


## Berechnung Gesamtnote Staatsprüfung
schriftliche_staatsprüfung_gesamt = berechnung_gesamtnote(schriftliche_staatsprüfung, 0)
mündliche_staatsprüfung_gesamt = berechnung_gesamtnote(mündliche_staatsprüfung, 0)

staatsprüfung_gesamt = verrechnung(schriftliche_staatsprüfung_gesamt, mündliche_staatsprüfung_gesamt, 0.7)
staatsprüfung_gesamt = float("%.2f" % (staatsprüfung_gesamt))
print ("\n")
durchgefallen (staatsprüfung_gesamt, "Staatsprüfung", schriftliche_staatsprüfung, 3.80)
notenstufe(staatsprüfung_gesamt)



## Eingabe Uniprüfung

# Seminararbeit
print ("\n Bitte geben Sie jetzt die Note der Seminararbeit ein.")
eingabe_prüfungen (1, seminar)
seminar_gesamt = berechnung_gesamtnote (seminar, 0)

# Uniprüfung
print ("\n Und schließlich die Note der letzten schriftlichen Universitätsprüfung.")
eingabe_prüfungen (1, uni_prüfung)
uni_prüfung_gesamt = berechnung_gesamtnote (uni_prüfung, 0)


## Berechnung Gesamtnote Uniprüfung
uni_prüfung_verrechnet = verrechnung (uni_prüfung_gesamt, seminar_gesamt, 0.5)
uni_prüfung_verrechnet = float ("%.2f" % (uni_prüfung_verrechnet))
print ("\n")
durchgefallen (uni_prüfung_verrechnet, "Universitätsprüfung", schriftliche_staatsprüfung, 4.00)
notenstufe (uni_prüfung_verrechnet)


## Berechnung Gesamtnote und Ergebnis
endnote = verrechnung (staatsprüfung_gesamt, uni_prüfung_gesamt, 0.7)
endnote = float ("%.2f" % (endnote))
print ("\n\n")
durchgefallen (staatsprüfung_gesamt, "Staatsprüfung", schriftliche_staatsprüfung, 4.00)
notenstufe(staatsprüfung_gesamt)
print ("\n\n")
referenz = 333
durchgefallen (endnote, "Erste Juristische Prüfung", schriftliche_staatsprüfung, 4.00)
notenstufe (endnote)
print ("\n\n")
