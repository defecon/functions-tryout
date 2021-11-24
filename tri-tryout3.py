def print_info(naam, leeftijd):
    print(f'Hallo {naam}, je leeftijd is {leeftijd} jaar')


while True:
    naam = input('Wat is uw naam? : ')
    leeftijd = input('Wat is uw leeftijd? :')
    Stop = input('de 2 vragen zijn beantwoord u kunt stoppen met het woord stop :')

    if Stop == 'stop':
        break


    print_info(naam, leeftijd)