import os
import random
import time
from console import utils

# utils.wait_key()
# utils.pause('Cekam..')

"""
penize za kolo = rand(5,11)*prumysl

- konec
- armada: koupit/prodat -> zepta se na cislo
- prumysl: stejne jako ^^^. Max 1/10 rozlohy
- sousedi: rand(2,6) - bude nejaky seznam. definovany vztahy s kazdym sousedem. soucasti vztahu je 'respekt' ovlivnujici pravdepodobnost udalosti.
"""

obtiznost_var = 1

while True:
    obtiznost = input("zvol si obtiznost (easy, normal, hard) ")
    if obtiznost == "easy":
        obtiznost_var = 1
        break
    elif obtiznost == "normal":
        obtiznost_var = 2
        break
    if obtiznost == "hard":
        obtiznost_var = 3
        break

penize = random.randrange(400, 500 * (4 - obtiznost_var), 10)
armada = random.randint(10, 40)
rozloha = random.randrange(50, 151, 10)
prumysl = random.randint(5, rozloha//10)

soused_1 = "hraje"
if soused_1 == "hraje":
    soused_1_armada = random.randint(5,20)
    soused_1_rozloha = random.randrange(40, 161, 10)
    soused_1_prumysl = random.randint(4, soused_1_rozloha//10)
    soused_1_utok = False
soused_2 = random.choice(('hraje', 'nehraje'))
if soused_2 == "hraje":
    soused_2_armada = random.randint(5,20)
    soused_2_rozloha = random.randrange(40, 161, 10)
    soused_2_prumysl = random.randint(4, soused_2_rozloha//10)
    soused_2_utok = False
soused_3 = random.choice(('hraje', 'nehraje'))
if soused_3 == "hraje":
    soused_3_armada = random.randint(5,20)
    soused_3_rozloha = random.randrange(40, 161, 10)
    soused_3_prumysl = random.randint(4, soused_3_rozloha//10)
    soused_3_utok = False
soused_4 = random.choice(('hraje', 'nehraje'))
if soused_4 == "hraje":
    soused_4_armada = random.randint(5,20)
    soused_4_rozloha = random.randrange(40, 161, 10)
    soused_4_prumysl = random.randint(4, soused_4_rozloha//10)
    soused_4_utok = False

kolo = 1
napoveda = True

prumysl_cost_sell = 40
prumysl_cost_buy = 50

rozloha_cost_sell = 4
rozloha_cost_buy = 5

armada_cost_sell = 15
armada_cost_buy = 20

def vypocet_zautoceni_nepritele(cislo_soused):
    if cislo_soused == 1:
        return (soused_1 == "hraje") and (soused_1_armada >= armada - 10) and (kolo >= 1 * 10 - obtiznost_var * 2) and ((random.randint(0,4 - obtiznost_var) == 0) or (kolo > 20))
    if cislo_soused == 2:
        return (soused_2 == "hraje") and (soused_2_armada >= armada - 10) and (kolo >= 2 * 10 - obtiznost_var * 2) and ((random.randint(0,4 - obtiznost_var) == 0) or (kolo > 30))
    if cislo_soused == 3:
        return (soused_3 == "hraje") and (soused_3_armada >= armada - 10) and (kolo >= 3 * 10 - obtiznost_var * 2) and ((random.randint(0,4 - obtiznost_var) == 0) or (kolo > 40))
    if cislo_soused == 4:
        return (soused_4 == "hraje") and (soused_4_armada >= armada - 10) and (kolo >= 4 * 10 - obtiznost_var * 2) and ((random.randint(0,4 - obtiznost_var) == 0) or (kolo > 50))
    
def print_variables():
    
    print()
    print('=' * 75)
    print(f"   mas: {penize} penez, {armada} armady, {rozloha} rozlohy, {prumysl} prumyslu a je kolo {kolo}")
    print('=' * 75)
    print(f"   za kolo se ti pricte: {prumysl * 10 - armada * 5}")
    print('=' * 75)

    if penize >= 1500 and napoveda:
        print("mas hodne penez, ktere muzes puzit, kup rozlohu, armadu nebo prumysl")
    if prumysl * 10 - armada * 5 < 0 and napoveda:
        print("oohhh NE! prodelavas penize kazde kolo! neco s tim udelej")

def ask_player():
    global kolo, rozloha, prumysl, armada, penize, soused_1_utok, soused_2_utok, soused_3_utok, soused_4_utok, soused_1_armada, soused_2_armada, soused_3_armada, soused_4_armada, napoveda, obtiznost_var

    player_input = input("kterou polozku chces koupit/prodat? (armada, rozloha, prumysl, nastaveni, konec): ")
    player_input = player_input.lower()

    if player_input == "armada":
        player_input = input("chces koupit nebo prodat armadu? (zpatky, koupit, prodat): ")
        if player_input == "zpatky":
            return
        elif player_input == "koupit":
            print(f"mas {penize} penez")
            player_input = input(f"kolik chces koupit armady? (1 = {armada_cost_buy}$, -5/kolo): ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input * armada_cost_buy < penize:
                    penize -= player_input * armada_cost_buy
                    armada += player_input
                    print(f"- {player_input * armada_cost_buy} penez")
                    utils.pause('Stiskni enter pro pokracovani..')
            else:
                return
        elif player_input == "prodat":
            print(f"mas {armada} armady")
            player_input = input(f"kolik chces prodat armady? (1 = {armada_cost_sell}$, +5/kolo): ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input <= armada:
                    penize += player_input * armada_cost_sell
                    armada -= player_input
                    print(f"+ {player_input * armada_cost_sell} penez")
                    utils.pause('Stiskni enter pro pokracovani..')
                else:
                    return

    elif player_input == "rozloha":
        player_input = input("chces koupit nebo prodat pudu? (zpatky, koupit, prodat): ")
        if player_input == "zpatky":
            return
        elif player_input == "koupit":
            print(f"mas {penize} penez")
            player_input = input(f"kolik chces koupit pudy? (1 = {rozloha_cost_buy}$): ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input * rozloha_cost_buy < penize:
                    penize -= player_input * rozloha_cost_buy
                    rozloha += player_input
                    print(f"- {player_input * rozloha_cost_buy} penez")
                    utils.pause('Stiskni enter pro pokracovani..')
            else:
                return

        elif player_input == "prodat":
            print(f"mas {rozloha} rozlohy")
            print(f'maximalne muzes prodat {rozloha - prumysl * 10}, protoze rozloha({rozloha}) nemuze byt nissi nez 1 prumysl na 10 rozlohay ({prumysl * 10})')
            player_input = input(f"kolik chces prodat pudy? (1 = {rozloha_cost_sell}$:) ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input <= rozloha - prumysl * 10 and player_input > 0:                              # and player_input >= rozloha - prumysl * 10
                    penize += player_input * rozloha_cost_sell
                    rozloha -= player_input
                    print(f"+ {player_input * rozloha_cost_sell} penez")
                    utils.pause('Stiskni enter pro pokracovani..')
                else:
                    return

    elif player_input == "prumysl":
        player_input = input("chces koupit nebo prodat prumysl? (zpatky, koupit, prodat): ")
        if player_input == "zpatky":
            return
        elif player_input == "koupit":
            print(f"mas {penize} penez")
            player_input = input(f"kolik chces koupit prumyslu? (1 = {prumysl_cost_buy}$, muzes mit maximum 1\10 rozlhy): ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input * prumysl_cost_buy <= penize and rozloha >= prumysl + player_input * 10:
                    penize -= player_input * prumysl_cost_buy
                    prumysl += player_input
                    print(f"- {player_input * prumysl_cost_buy} penez")
                    utils.pause('Stiskni enter pro pokracovani..')
            else:
                return
        elif player_input == "prodat":
            print(f"mas {prumysl} prumyslu")
            player_input = input(f"kolik chces prodat prumyslu? (1 = {prumysl_cost_sell}$:) ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input <= prumysl:
                    penize += player_input * prumysl_cost_sell
                    prumysl -= player_input
                    print(f"{player_input * prumysl_cost_sell} penez")
                    utils.pause('Stiskni enter pro pokracovani..')
                else:
                    return
                

    elif player_input == "nastaveni":
        player_input = input("co chces zmenit? (obtiznost, napoveda): ")
        if player_input == "obtiznost":
                while True:
                    obtiznost = input("zvol si obtiznost (easy, normal, hard) ")
                    if obtiznost == "easy":
                        obtiznost_var = 1
                        print("zmnenil jsi obtiznost na EASY")
                        break
                    elif obtiznost == "normal":
                        obtiznost_var = 2
                        print("zmnenil jsi obtiznost na NORMAL")
                        break
                    if obtiznost == "hard":
                        obtiznost_var = 3
                        print("zmnenil jsi obtiznost na HARD")
                        break
                utils.pause('Stiskni enter pro pokracovani..')

        if player_input == "napoveda":
            player_input = input("chces mit zaplou napovedu? (ANO, NE)")
            if player_input == "ano":
                napoveda = True
            elif player_input == "ne":
                napoveda = False
            utils.pause('Stiskni enter pro pokracovani..')

    elif player_input == "konec":
        penize_za_kolo =  prumysl * 10
        odcteni_za_kolo = 5 * armada
        celkove_penize_za_kolo = penize_za_kolo - odcteni_za_kolo
        penize += celkove_penize_za_kolo
        if celkove_penize_za_kolo < 0:
            print(f"prodelavas penize za kolo :( zkus to zpravit")
            print(f"{celkove_penize_za_kolo}")
        else:
            print(f"+ {celkove_penize_za_kolo}")
        
        utils.pause('Stiskni enter pro pokracovani..')

        if soused_1_utok:
            print("TVUJ SOUSED 1 TE NAPADL!, skus se ubranit")
            armada -= 5 + 5 * obtiznost_var
            soused_1_armada -= soused_1_armada // 100 * 90
            utils.pause('Stiskni enter pro pokracovani..')
        else:
            if soused_1 == "hraje":
                soused_1_utok = vypocet_zautoceni_nepritele(1)

        if soused_2_utok:
            print("TVUJ SOUSED 2 TE NAPADL!, skus se ubranit")
            armada -= 5 + 5 * obtiznost_var
            soused_2_armada -= soused_2_armada // 100 * 90
            utils.pause('Stiskni enter pro pokracovani..')
        else:
            if soused_2 == "hraje":
                soused_2_utok = vypocet_zautoceni_nepritele(2)

        if soused_3_utok:
            print("TVUJ SOUSED 3 TE NAPADL!, skus se ubranit")
            armada -= 5 + 5 * obtiznost_var
            soused_3_armada -= soused_3_armada // 100 * 90
            utils.pause('Stiskni enter pro pokracovani..')
        else:
            if soused_3 == "hraje":
                soused_3_utok = vypocet_zautoceni_nepritele(3)
        if soused_4_utok:
            print("TVUJ SOUSED 4 TE NAPADL!, skus se ubranit")
            armada -= 5 + 5 * obtiznost_var
            soused_4_armada -= soused_4_armada // 100 * 90
            utils.pause('Stiskni enter pro pokracovani..')
        else:
            if soused_4 == "hraje":
                soused_4_utok = vypocet_zautoceni_nepritele(4)


        kolo += 1

soused_1_utok = False
soused_2_utok = False
soused_3_utok = False
soused_4_utok = False

while armada >= 0 and rozloha >= 0:

    print_variables()
    ask_player()

print("=" * 50)
print("PROHRAL JSI")
print("=" * 50)
