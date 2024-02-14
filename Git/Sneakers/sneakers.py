from pprint import pprint


def beolvasas():
    cipok = []
    with open('sneakers.csv', 'r', encoding='utf-8') as fajl:
        sorok = fajl.readlines()
        keys = sorok[0].strip().split(',')
        print(sorok)
        for sor in sorok[1:]:
            ertek = sor.strip().split(',')
            cipok.append(dict(zip(keys, ertek)))
    return cipok


def kiiras(cipok, rendezes):
    for cipo in cipok:
        cipo['full_price'] = float(cipo['full_price'])
        cipo['current_price'] = float(cipo['current_price'])

    if rendezes == 1:
        rendezes = 'title'
    elif rendezes == 2:
        rendezes = 'color'
    elif rendezes == 3:
        rendezes = 'full_price'
    elif rendezes == 4:
        rendezes = 'current_price'
    elif rendezes == 5:
        rendezes = 'publish_date'
    rendezett_cipok = sorted(cipok, key=lambda x: x[rendezes])
    for cipo in rendezett_cipok:
        pprint(cipo)


def main():
    cipok = beolvasas()
    print(
        "Válassz, melyik szempont alapján rendezzem a cipőket? \n 1 - title \n 2 - color \n 3 - full price \n 4 - "
        "current price \n 5 - publish date")
    rendezes = int(input("Add meg a lehetőség számát! "))
    kiiras(cipok, rendezes)


main()
