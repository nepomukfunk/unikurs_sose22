# Einheit 1 - Blutalkoholspiegel
# (C) 30.04.2022, Christian Thomas

masseAlkohol: float = 0
literAlkohol: float = 0
prozent: float = 0
massePerson: float = 0
reduktion = 0
blutalkohol = 0



# Überschrift
print("Dieses Programm berechnet den Blutalkoholwert nach der 'Widmark - Formel' ")
print("\n")


# Liter Alkohol
print("Wie viele Liter Alkohol haben Sie getrunken (Bsp. '1.3') ?")
literAlkohol = float (input () )
print("\n")


# Prozent
print ("Wie viel Prozent Alkohol hatte das Getränk (Bsp. '5.4') ?")
prozent = float (input () )
print("\n")


# Masse Person
print ("Was ist Ihr Gewicht in Kilogramm (Bsp. '73.5') ?")
massePerson  = float (input () )
print("\n")


# Geschlecht
print("Was ist Ihr Geschlecht (f/m) ?")
eingabeGeschlecht :str = input()
if eingabeGeschlecht == "f":
    reduktion = 0.6
else:
    reduktion = 0.7
print("\n")


# Berechnung Masse Alkohol
masseAlkohol = literAlkohol * 1000 * prozent / 100 * 0.8 


# Berechnung Blutalkohol
blutalkohol = round ( masseAlkohol / (massePerson * reduktion) , 2)


# Ergebnis
print ("Ihr Blutalkoholwert in Promille beträgt:    %.2f" % (blutalkohol) )
print("\n")

# Auswirkung
print ("Auswirkungen:")


if blutalkohol < 0.1:
    print ("Enthemmung, kontaktfreudiger als vorher, gelöste Stimmung, erste Fehleinschätzungen")
if blutalkohol >= 0.1 and blutalkohol < 0.8 :
    print ("Fehlende Konzentration, Tunnelblick, verlängerte Reaktionszeit, etc.")
if blutalkohol >= 0.8:
    print ("Unkoordinierte Bewegung, Erbrechen, Muskelerschlaffung, etc.")
print("\n")
print("\n")
