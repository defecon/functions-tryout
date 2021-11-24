def addition(aantal):
    for i in range (aantal):
        print(f'{getal1} + {getal2} = {getal1+getal2}')

getal1 = int(input("Voer hier een getal in : "))
getal2 = int(input("Voer hier een getal in : "))

print("\n------------------------\n")

def subtraction(aantal):
    for i in range (aantal):
        print(f'{getal3} - {getal4} = {getal3-getal4}')

getal3 = int(input("Voer hier een getal in : "))
getal4 = int(input("Voer hier een getal in : "))

print("\n------------------------\n")

def multiplication(aantal):
    for i in range (aantal):
        print(f'{getal5} x {getal6} = {getal5*getal6}')

getal5 = int(input("Voer hier een getal in : "))
getal6 = int(input("Voer hier een getal in : "))

print("\n------------------------\n")

def division(aantal):
    for i in range (aantal):
        print(f'{getal7} : {getal8} = {getal7 / getal8}')

getal7 = int(input("Voer hier een getal in : "))
getal8 = int(input("Voer hier een getal in : "))

print("\n------------------------\n")

def increment(aantal):
    for i in range(aantal):
        print(f'{getal9} + {1} = {getal9 + 1}')
    
getal9 = int(input("Voer hier een getal in :"))

print("\n------------------------\n")

def decrement(aantal):
    for i in range(aantal):
        print(f'{getal10} - {1} = {getal10 - 1}')

getal10 = int(input("Voer hier een getal in :"))

print("\n------------------------\n")

addition(1)
subtraction(1)
multiplication(1)
division(1)
increment(1)
decrement(1)