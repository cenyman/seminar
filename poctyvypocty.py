import math

def krychle(delka_strany):
    obsah = delka_strany * delka_strany * 6 
    objem = delka_strany* delka_strany * delka_strany
    return obsah, objem

def kvadr(delka, sirka, vyska):
    obsah = 2 * (delka * sirka + delka * vyska + sirka * vyska)
    objem = delka * sirka * vyska
    return obsah, objem

def koule(polomer):
    obsah = 4 * math.pi * polomer*polomer
    objem = (4/3) * math.pi * polomer*polomer*polomer
    return obsah, objem

def ctverec(delkaa):
    obsah = delkaa*delkaa
    return obsah

def obdelnik(delka, sirka):
    obsah = delka * sirka
    return obsah

def kruh(polomer):
    obsah = math.pi * polomer**2
    return obsah

def main():
    while True:
        print("Vyberte si teleso pro vypocet (1 krychle, 2 kvadr, 3 koule, 4 ctverec, 5 obdelnik, 6 kruh, 0 ukoncit):")
        vyber = int(input())
        
        if vyber == 0:
            break
        elif vyber in [1, 2, 3, 4, 5, 6]:
            print("Vyberte co chcete pocitat (1 obsah, 2 objem):")
            vyber_vypocet = int(input())
            
            if vyber_vypocet == 1:
                if vyber == 1:
                    delkaa = float(input("Zadejte delku krychle: "))
                    obsah, _ = krychle(delkaa)
                elif vyber == 2:
                    delka = float(input("Zadejte delku kvadru: "))
                    sirka = float(input("Zadejte sirku kvadru: "))
                    vyska = float(input("Zadejte vysku kvadru: "))
                    obsah, _ = kvadr(delka, sirka, vyska)
                elif vyber == 3:
                    polomer = float(input("Zadejte polomer koule: "))
                    obsah, _ = koule(polomer)
                elif vyber == 4:
                    delkaa = float(input("Zadejte delku ctverce: "))
                    obsah = ctverec(delkaa)
                elif vyber == 5:
                    delka = float(input("Zadejte delku obdelniku: "))
                    sirka = float(input("Zadejte sirku obdelniku: "))
                    obsah = obdelnik(delka, sirka)
                elif vyber == 6:
                    polomer = float(input("Zadejte polomer circle: "))
                    obsah = kruh(polomer)
                
                print(f" Obsah: {obsah:.2f}")
            elif vyber_vypocet == 2:
                if vyber == 1:
                    delkaa = float(input("Zadejte delku krychle: "))
                    _, objem = krychle(delkaa)
                elif vyber == 2:
                    delka = float(input("Zadejte delku kvadru: "))
                    sirka = float(input("Zadejte sirku kvadru: "))
                    vyska = float(input("Zadejte vysku kvadru: "))
                    _, objem = kvadr(delka, sirka, vyska)
                elif vyber == 3:
                    polomer = float(input("Zadejte polomer koule: "))
                    _, objem = koule(polomer)
                else:
                    print("Neplatny vyber.")
                    continue
                
                print(f"objem: {objem:.2f}")
            else:
                print("Neplatny vypocet.")
                continue
        else:
            print("Neplatny utvar. Zadejte 1, 2, 3, 4, 5, 6, nebo 0 pro ukonceni .")
            continue
        
        print()

if __name__ == "__main__":
    main()


#source: chat.openai.com
