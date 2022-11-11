#import section
import calendar
import random
from array import*
import os
import string

#Programs defining section
#1
def dodawanie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik dodawania, to ",liczba1 + liczba2)
    menu()
#2
def odejmowanie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik odejmowania, to ",liczba1 - liczba2)
    menu()
#3
def mnozenie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik mnożenia, to ",liczba1 * liczba2)
    menu()
#4
def dzielenie_całkowite_bez_reszty():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik dzielenia calkowitego (bez reszty), to ",int(liczba1 / liczba2))
    menu()
#5
def modulo_reszta_z_dzielenia():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Reszta z dzielenia, to ",liczba1 % liczba2)
    menu()
#6
def dzielenie_z_reszta():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik dzielenia, to ",int(liczba1 / liczba2), "z resztą, równą: ",liczba1 % liczba2)
    menu()
#7
def potegowanie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj potęgę.\n"))
    print("Wynik potęgowania twojej liczby, to ",liczba1 ** liczba2)
    menu()
#8
def kalendarz():
    rok = int(input("Podaj rok"))
    miesiac = int(input("Podaj miesiac"))
    print('  Python Calendar\n ')
    print(calendar.month(rok,miesiac))
    menu()
#9
def zgadnij_liczbe():
    print("Podaj liczbe")
    liczba = int(input())
    liczba_losowa = int(random.randint(1, 10))
    while not(liczba == liczba_losowa):
        if(liczba < liczba_losowa):
            print("To nie ta liczba")
            print("Podaj większą liczbę")
            liczba = int(input())
        elif (liczba > liczba_losowa):
            print("To nie ta liczba")
            print("Podaj mniejszą liczbę")
            liczba = int(input())
    print("Wpisałeś dobrą liczbę")
    print("Kończę program")
    menu()
#10
def quiz_matematyczny_dodawanie():
    print("Witam w quizie, dodawanie")
    wynik = 0
    i=0
    while(i<5):
        print("Odpowiedz na moje pytanie:")
        liczba1 = int(random.randint(1, 100))
        liczba2 = int(random.randint(1, 100))
        print("Ile rowna sie: ",liczba1 ," + ",liczba2," = ?\n")
        liczba = int(input())
        i += 1
        if (liczba == liczba1 + liczba2):
            wynik += 1
            print("Brawo!")
    print("Twój wynik, to: ",wynik)
    menu()
#11
def quiz_matematyczny_odejmowanie():
    print("Witam w quizie odejmowanie")
    wynik = 0
    i=0
    while(i<5):
        print("Odpowiedz na moje pytanie:")
        liczba1 = int(random.randint(1, 100))
        liczba2 = int(random.randint(1, 100))
        print("Ile rowna sie: ",liczba1 ," - ",liczba2," = ?\n")
        liczba = int(input())
        i += 1
        if (liczba == liczba1 - liczba2):
            wynik += 1
            print("Brawo!")
    print("Twój wynik, to: ",wynik)
    menu()
#12
def quiz_matematyczny_mnozenie():
    print("Witam w quizie mnozenie")
    wynik = 0
    i=0
    while(i<5):
        print("Odpowiedz na moje pytanie:")
        liczba1 = int(random.randint(1, 100))
        liczba2 = int(random.randint(1, 100))
        print("Ile rowna sie: ",liczba1 ," * ",liczba2," = ?\n")
        liczba = int(input())
        i += 1
        if (liczba == liczba1 * liczba2):
            wynik += 1
            print("Brawo!")
    print("Twój wynik, to: ",wynik)
    menu()
#13
def zgadnij_kolor():
    
    print("Moje kolory: czerwony, niebieski, cyanowy, rozowy, zielony")
    print("Prosze wybierz jeden z kolorow, zobaczymy czy wybierzesz ten sam kolor, ktory wybralem ja")
    color = random.choice(["czerwony", "niebieski", "cyanowy", "rozowy", "zielony"])
    choose = input()
    while(choose != color):
        print("Zly kolor")
        if(color == "czerwony"):
            print("Jestes teraz dosyc CZERWONY ?")
            choose = input()
        elif (color == "niebieski"):
            print("Jestes teraz dosyc NIEBIESKI ?")
            choose = input()
        elif (color == "cyanowy"):
            print("Jestes teraz dosyc CYANOWY ?")
            choose = input()
        elif (color == "rozowy"):
            print("Jestes teraz dosyc ROZOWY ?")
            choose = input()
        elif (color == "zielony"):
            print("Jestes teraz dosyc ZIELONY ?")
            choose = input()
    if(choose == color):
        print("Brawo, wybrales ten sam kolor co ja!")
    menu()
#14
def tuple_indexy():
    kraje = ("Polska", "Francja", "Niemcy", "Argentyna", "Hiszpaia")
    print(kraje)
    print("Wpisz jeden z podanych przeze mnie krajów, proszę.")
    wybor = input()
    index = kraje.index(wybor)
    print("Numer indeksu (W tupli) wybranego przez ciebie kraju, to: ", index)
    kraje = ("Polska", "Francja", "Niemcy", "Argentyna", "Hiszpaia")
    print("Mam tuple, wybierz numer indeksu, a ja wyświetlę jaki to jest kraj!")
    wybor = int(input())
    print(kraje[wybor])
    menu()
#15
def lista_zaproszonych():
    zaproszeni = []
    print("Wpisz 3 osoby, po enterze, kóre chcesz zaprosić na swoją imprezę?")
    zaproszeni += (input(), input(), input())
    print("Czy chcesz dodac kolejna osobe?")
    wybor = input()
    while (wybor != "nie"):
        print("Wpisz osobę")
        zaproszeni += (input(),)
        print("Czy chcesz dodac kolejna osobe?")
        wybor = input()
    print("Zaprosiłeś ",len(zaproszeni)," osób!")
    menu()
#16
def wyraz_w_pionie():
    word = input("Wprowadź słowo: ")
    length = len(word)
    num = 1
    for x in word:
        position = length - num
        letter = word[position]
        print(letter)
        num = num + 1
    menu()
#17
def znajdz_najwieksza_liczbe():
    num1 = float(input("Wprowadz pierwszy numer: "))
    num2 = float(input("Wprowadz drugi numer: "))
    num3 = float(input("Wprowadz trzeci numer: "))

    if (num1 >= num2) and (num1 >= num3):
      wynik = num1
    elif (num2 >= num1) and (num2 >= num3):
       wynik = num2
    else:
       wynik = num3
    print("Największą liczbą jest: ", wynik)

    menu()
#18
def tabliczka_mnozenia_wybranej_liczby():
    num = int(input("Podaj liczbe, a ja wyswietle tabliczke mnozenia "))
    i = int(1)
    while i < 11:
        print(num, 'x', i, '=', num*i)
        i+=1
    menu()
#19
def liczba_na_rozne_systemy_liczbowe():

    liczba = int(input("Wpisz liczbę."))

    print("Liczba ", liczba, " to inaczej:")
    print(bin(liczba), "w systemie dwojkowym.")
    print(oct(liczba), "w systemie osemkowym.")
    print(hex(liczba), "w systemie szesnastkowym.")

    menu()
#20
def tworzenie_pliku_tekstowego():
    nazwa = input("Podaj nazwę pliku ('rozszerzenie txt')\n") + ".txt"
    file = open(nazwa, "w")
    file.close()
    print("plik ",nazwa," zostal utworzony")
    menu()
#21
def otworzenie_pliku_tekstowego():
    nazwa = input("Podaj nazwę pliku ('rozszerzenie txt')\n") + ".txt"
    if os.path.exists(nazwa):
        file = open(nazwa, "r")
        print(file.read())
        file.close()
    else:
        print("plik ",nazwa," nie istnieje")
    menu()
#22
def dopisywanie_do_pliku_tekstowego():
    nazwa = input("Podaj nazwę pliku ('rozszerzenie txt')\n") + ".txt"
    if os.path.exists(nazwa):
        file = open(nazwa, "a")
        wartosc = input("Wpisz to co chcesz dopisać do pliku\n")
        file.write(wartosc)
        file.close()
    else:
        print("plik ",nazwa," nie istnieje")
    menu()
#23
def usuwanie_pliku_tekstowego():
    nazwa = input("Podaj nazwę pliku ('rozszerzenie txt')\n") + ".txt"
    if os.path.exists(nazwa):
        os.remove(nazwa)
    else:
        print("plik ",nazwa," nie istnieje")
    menu()
#24
def pokaz_kod_ascii():
    znak = input("Podaj wybrany znak\n")
    print("Kod ASCII znaku ",znak," , to:\n")
    print(ord(znak))
    menu()
#25 
def zamien_dni():
    dni = int(input("Wprowadz liczbe dni\n"))
    rok = dni/365
    godziny = dni*24
    minuty = godziny*60
    sekundy = minuty*60
    print(dni," dni, to",rok," normalnego roku, ",godziny," godzin, ", minuty," minut, ",sekundy," sekund.")
    menu()
#26
def zamien_kilogramy():
    kg = int(input("Wprowadz liczbe kilogarmow\n"))
    tona = kg/1000
    dekagramy = kg*100
    gramy = kg*1000
    miligramy = gramy*1000
    print(kg," kg, to",tona," tony, ",dekagramy," dekagramow, ", gramy," gramow, ",miligramy," miligramow.")
    menu()
#27
def zamien_metry():
    m = int(input("Wprowadz liczbe metrow\n"))
    km = m*1000
    cm = m*100
    mm = cm*10
    print(m," metrow, to",km," kilometra, ",cm," centymetrow, ",mm," milimetrow.")
    menu()
#28
def policz_znaki():
    tekst = input("Wprowadz swoj tekst\n")
    dlugosc = len(tekst)
    print("Twoj tekst, ma ",dlugosc," znakow.")
    menu()
#29
def oblicz_bmi():
    wysokosc = float(input("Ile mierzysz wzrostu? (w metrach)\n"))
    waga = float(input("Jaka jest twoja waga? (w kilogramach)\n"))

    bmi = waga / (wysokosc ** 2)
    print(bmi)
    if bmi < 15:
        print("bardzo duza niedowaga")
    elif bmi < 16:
        print("duza niedowaga")
    elif bmi < 18.5:
        print("niedowaga")
    elif bmi < 25:
        print("Normalne, dobre, zdrowe BMI")
    elif bmi < 30:
        print("Nadwaga")
    elif bmi < 35:
        print("Otylosc klasa I")
    elif bmi < 40:
        print("Otylosc klasa II")
    else:
        print("Otylosc klasa III")
    menu()
#30
lista = []
def lista_do_zrobienia():
    print('''
    1.Dodawanie rekordu
    2.Wyswietlanie rekordu
    3.Usuwanie rekordu
    4.Usuwanie wszystkich rekordow
    5.Powrot do menu
    ''')
    pytanie = int(input("Wybierz jedna z opcji?\n"))
    if(pytanie==1):
        rekord = input("Co chcesz dodac?\n")
        lista.append(rekord)
        input("Wcisnij Enter aby przejsc dalej")
        lista_do_zrobienia()
    elif(pytanie==2):
        print(lista)
        input("Wcisnij Enter aby przejsc dalej")
        lista_do_zrobienia()
    elif(pytanie==3):
        print(lista)
        rekord = int(input("Ktory rekord chcesz usunac?\n"))
        print("Usuwam rekord ",lista[rekord])
        lista.pop(rekord)
        input("Wcisnij Enter aby przejsc dalej")
        lista_do_zrobienia()
    elif(pytanie==4):
        rekord = input("Czy jestes pewien?(t/n)\n")
        if(rekord=="t"):
            print("Usunieto wszystkie rekordy z listy")
            lista.clear()
            input("Wcisnij Enter aby przejsc dalej")
            lista_do_zrobienia()
        else:
            print("Dokonano zlego wyboru, nic nie zrobilem")
            input("Wcisnij Enter aby przejsc dalej")
            lista_do_zrobienia()
    elif(pytanie==5):
        menu()
    else:
        print("Nie wybrano zadnegj dostepnej opcji\n")
        input("Wcisnij Enter aby przejsc dalej")

#Defining menu-main program
def menu():
    input("Wcisnij Enter aby przejsc dalej")
    print('''
        Lista dostępnych programow:
        1.dodawanie
        2.odejmowanie
        3.mnozenie
        4.dzielenie całkowite bez reszty
        5.modulo, reszta z dzielenia
        6.dzielenie_z_reszta
        7.potegowanie
        8.kalendarz
        9.zgadnij_liczbe
        10.quiz_matematyczny_dodawanie
        11.quiz_matematyczny_odejmowanie
        12.quiz_matematyczny_mnozenie
        13.zgadnij_kolor
        14.tuple_indexy
        15.lista_zaproszonych
        16.wyraz_w_pionie
        17.znajdz_najwieksza_liczbe
        18.tabliczka_mnozenia_wybranej_liczby
        19.liczba_na_rozne_systemy_liczbowe
        20.tworzenie_pliku_tekstowego
        21.otworzenie_pliku_tekstowego
        22.dopisywanie_do_pliku_tekstowego
        23.usuwanie_pliku_tekstowego
        24.pokaz_kod_ascii
        25.zamien_dni
        26.zamien_kilogramy
        27.zamien_metry
        28.policz_znaki
        29.oblicz_bmi
        30.lista_do_zrobienia
        31.Wyjście-zakonczenie-dzialania-programu
    ''')

    wybor = input("Wbyierz program z powyzszych \n")
    match wybor:
        case "1":
            dodawanie()
        case "2":
            odejmowanie()
        case "3":
            mnozenie()    
        case "4":
            dzielenie_całkowite_bez_reszty()
        case "5":
            modulo_reszta_z_dzielenia()
        case "6":	
            dzielenie_z_reszta()
        case "7":	
            potegowanie()
        case "8":	
            kalendarz()
        case "9":	
            zgadnij_liczbe()
        case "10":	
            quiz_matematyczny_dodawanie()
        case "11":	
            quiz_matematyczny_odejmowanie()
        case "12":	
            quiz_matematyczny_mnozenie()
        case "13":	
            zgadnij_kolor()
        case "14":	
            tuple_indexy()
        case "15":	
            lista_zaproszonych()
        case "16":	
            wyraz_w_pionie()
        case "17":	
            znajdz_najwieksza_liczbe()
        case "18":	
            tabliczka_mnozenia_wybranej_liczby()
        case "19":	
            liczba_na_rozne_systemy_liczbowe()
        case "20":	
            tworzenie_pliku_tekstowego()
        case "21":	
            otworzenie_pliku_tekstowego()
        case "22":	
            dopisywanie_do_pliku_tekstowego()
        case "23":	
            usuwanie_pliku_tekstowego()
        case "24":	
            pokaz_kod_ascii()
        case "25":	
            zamien_dni()
        case "26":	
            zamien_kilogramy()
        case "27":	
            zamien_metry()
        case "28":	
            policz_znaki()
        case "29":	
            oblicz_bmi()
        case "30":	
            lista_do_zrobienia()
        case "31":
            quit()
        case _:
            print("Proszę wpisz dobry numer.")
            menu()

menu()