import os
import random
import time
"""
penize za kolo = rand(5,11)*prumysl

- konec
- armada: koupit/prodat -> zepta se na cislo
- prumysl: stejne jako ^^^. Max 1/10 rozlohy
- sousedi: rand(2,6) - bude nejaky seznam. definovany vztahy s kazdym sousedem. soucasti vztahu je 'respekt' ovlivnujici pravdepodobnost udalosti.
"""

penize = random.randrange(100, 1000, 5)
armada = random.randint(10, 50)
rozloha = random.randrange(50, 151, 10)
prumysl = random.randint(5, rozloha//10)

soused_1 = "hraje"
if soused_1 == "hraje":
    soused_1_armada = random.randint(5,20)
    soused_1_rozloha = random.randrange(40, 161, 10)
    soused_1_prumysl = random.randint(4, soused_1_rozloha//10)
soused_2 = random.choice(('hraje', 'nehraje'))
if soused_2 == "hraje":
    soused_2_armada = random.randint(5,20)
    soused_2_rozloha = random.randrange(40, 161, 10)
    soused_2_prumysl = random.randint(4, soused_2_rozloha//10)
soused_3 = random.choice(('hraje', 'nehraje'))
if soused_3 == "hraje":
    soused_3_armada = random.randint(5,20)
    soused_3_rozloha = random.randrange(40, 161, 10)
    soused_3_prumysl = random.randint(4, soused_3_rozloha//10)
soused_4 = random.choice(('hraje', 'nehraje'))
if soused_4 == "hraje":
    soused_4_armada = random.randint(5,20)
    soused_4_rozloha = random.randrange(40, 161, 10)
    soused_4_prumysl = random.randint(4, soused_4_rozloha//10)

kolo = 1

prumysl_cost_sell = 40
prumysl_cost_buy = 50

rozloha_cost_sell = 4
rozloha_cost_buy = 5

armada_cost_sell = 15
armada_cost_buy = 20

def print_variables():
    print()
    print('=' * 50)
    print(f"mas: {penize} penez, {armada} armady, {rozloha} rozlohy, {prumysl} prumyslu a je kolo {kolo}")
    print('=' * 50)
    print()

def ask_player():
    global kolo

    player_input = input("kterou polozku chces koupit/prodat? (armada, rozloha, prumysl, konec): ")
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
                if player_input * prumysl_cost_buy < penize and rozloha >= prumysl + player_input * 10:
                    penize -= player_input * prumysl_cost_buy
                    prumysl += player_input
                    print(f"- {player_input * prumysl_cost_buy} penez")
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
                else:
                    return

    elif player_input == "konec":
        penize_za_kolo =  prumysl * random.randint(5, 11)
        odcteni_za_kolo = 5 * armada
        celkove_penize_za_kolo = penize_za_kolo - odcteni_za_kolo
        penize += celkove_penize_za_kolo
        if celkove_penize_za_kolo < 0:
            print(f"prodelavas penize za kolo :(, skus to zpravit")
            print(f"{celkove_penize_za_kolo}")
        else:
            print(f"+ {celkove_penize_za_kolo}")
        
        kolo += 1

while armada >= 0 and rozloha >= 0:

    print_variables()
    ask_player()




print("=" * 50)
print("PROHRAL JSI")
print("=" * 50)
