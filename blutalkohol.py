#april 2022

# classes & predefined values
class Beverage:

    def __init__(self, value=0):
        self.value = value

consumed_beer = Beverage()
consumed_wine = Beverage()
consumed_liquor = Beverage()

liters_bottle_beer = 0.5
liters_glass_wine = 0.15
liters_shot_liquor = 0.02

percentage_alc_beer = 0.05
percentage_alc_wine = 0.09
percentage_alc_liquor = 0.4

# 1 input relevant data
# ask for consumed beverages
all_beverages = input("Welche alkoholischen Getränke haben Sie konsumiert?").lower()

if "bier" in all_beverages:
    try:
        consumed_beer.value = float(input("Wie viele Flaschen Bier haben Sie getrunken?"))
    except ValueError:
        print("Bitte geben Sie nur Zahlen (nicht ausgeschrieben) ein!")
if "wein" in all_beverages:
    try:
        consumed_wine.value = float(input("Wie viele Gläser Wein haben Sie getrunken?"))
    except ValueError:
        print("Bitte geben Sie nur Zahlen (nicht ausgeschrieben) ein!")
if "schnaps" in all_beverages:
    try:
        consumed_liquor.value = int(input("Wie viele Shots harten Alkohol haben Sie getrunken?"))
    except ValueError:
        print("Bitte geben Sie nur ganze Zahlen (nicht ausgeschrieben) ein!")

# ask for body weight
try:
    body_weight = float(input("Wie viele Kilogramm wiegen Sie?"))
except ValueError:
    print("Bitte geben sie nur Zahlen (nicht ausgeschrieben) ein!")

# ask for gender to get body-liquid-share
gender = input("Sind Sie männlich (m), weiblich (w) oder keiner der beiden Kategorien zuzuordnen (d)?").lower()
if "m" in gender:
    body_liquid_share = 0.68
elif "w" in gender:
    body_liquid_share = 0.55
elif "d" in gender:
    body_liquid_share = round((0.68 + 0.55) / 2, 2)

# 2 calculate values
# calculate consumed liters of beverages
consumed_liters_of_beer = consumed_beer.value * liters_bottle_beer
consumed_liters_of_wine = consumed_wine.value * liters_glass_wine
consumed_liters_of_liquor = consumed_liquor.value * liters_shot_liquor

# calculate gramms of alcohol of consumed beverages
consumed_alc_gramm_beer = consumed_liters_of_beer * percentage_alc_beer
consumed_alc_gramm_wine = consumed_liters_of_wine * percentage_alc_wine
consumed_alc_gramm_liquor = consumed_liters_of_liquor * percentage_alc_liquor

# calculate total consumed alc
total_consumed_alc_in_gramm = consumed_alc_gramm_beer + consumed_alc_gramm_wine + consumed_alc_gramm_liquor

# calculate blood alcohol level
blood_alc_level = round(((total_consumed_alc_in_gramm / (body_weight * body_liquid_share)) * 100), 2)

# 3 output
statement_blood_alc_level = f"Ihre Blutalkoholkonzentration beträgt {blood_alc_level} Promill. "

if blood_alc_level <= 0.1:
    print(statement_blood_alc_level, "Ihre motorischen und geistigen Fähigkeiten sollten noch weitgehend uneingeschränkt sein :)")
elif blood_alc_level <= 0.3:
    print(statement_blood_alc_level, "Ihre motorischen und geistigen Fähigkeiten sind eingeschränkt!")
elif blood_alc_level <= 1:
    print(statement_blood_alc_level, "Lassen Sie sich lieber nach Hause bringen!")
elif blood_alc_level > 1:
    print(statement_blood_alc_level, "Sie trinken gefährlich viel Alkohol.")
