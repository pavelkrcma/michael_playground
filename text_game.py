import os
import random
"""
penize
armada
prumysl
sousedi
rozloha

penize za kolo = rand(5,11)*prumysl

- konec
- armada: koupit/prodat -> zepta se na cislo
- prumysl: stejne jako ^^^. Max 1/10 rozlohy
- sousedi: rand(2,6) - bude nejaky seznam. definovany vztahy s kazdym sousedem. soucasti vztahu je 'respekt' ovlivnujici pravdepodobnost udalosti.
"""

penize = random.randrange(100, 1000, 5)
armada = random.randint(10, 50)
rozloha = random.randint(50, 150)
prumysl = random.randint(5, rozloha//10)

def print_variables():
    print()
    print('=' * 50)
    print(f"mas: {penize} penez, {armada} armady, {rozloha} rozlohy a {prumysl} prumyslu")
    print('=' * 50)
    print()

while armada >= 0 and rozloha >= 0:
    
    print_variables()

    player_input = input("kterou polozku chces koupit/prodat? (armada, rozloha, prumysl): ")

    if player_input.lower() == "armada":
        player_input = input("chces koupit nebo prodat armadu? (zpatky, koupit, prodat): ")
        if player_input == "zpatky":
            continue
        if player_input == "koupit":
            print(f"mas {penize} penez")
            player_input = input("kolik chces koupit armady? (1 = 20$, -5/kolo): ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input * 20 < penize:
                    penize -= player_input * 20
                    armada += player_input
            else:
                continue
        if player_input == "prodat":
            print(f"mas {armada} armady")
            player_input = input("kolik chces prodat armady? (1 = 20$, -5/kolo): ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input <= armada:
                    penize += player_input * 15
                    armada -= player_input
                else:
                    continue
    if player_input == "rozloha":
        player_input = input("chces koupit nebo prodat pudu? (zpatky, koupit, prodat): ")
        if player_input == "zpatky":
            continue
        if player_input == "koupit":
            print(f"mas {penize} penez")
            player_input = input("kolik chces koupit pudy? (1 = 5$): ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input * 20 < penize:
                    penize -= player_input * 5
                    rozloha += player_input
            else:
                continue
        if player_input == "prodat":
            print(f"mas {rozloha} rozlohy")
            player_input = input("kolik chces prodat pudy? (1 = 5$:) ")
            if player_input.isdecimal():
                player_input = int(player_input)
                if player_input <= rozloha:
                    penize += player_input * 4
                    rozloha -= player_input
                else:
                    continue
            

print("=" * 50)
print("PROHRAL JSI")
print("=" * 50)