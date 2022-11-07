def dodawanie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik dodawania, to ",liczba1 + liczba2)
    menu()

def odejmowanie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik odejmowania, to ",liczba1 - liczba2)
    menu()

def mnozenie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik mnożenia, to ",liczba1 * liczba2)
    menu()

def dzielenie_całkowite_bez_reszty():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik dzielenia, to ",liczba1 / liczba2)
    menu()

def modulo_reszta_z_dzielenia():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Reszta z dzielenia, to ",liczba1 % liczba2)
    menu()

def dzielenie_z_reszta():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj druga liczbe.\n"))
    print("Wynik dzielenia, to ",liczba1 / liczba2, "z resztą, równą: ",liczba1 % liczba2)
    menu()

def potegowanie():
    liczba1 = int(input("Podaj pierwsza liczbe.\n"))
    liczba2 = int(input("Podaj potęgę.\n"))
    print("Wynik potęgowania twojej liczby, to ",liczba1 ^ liczba2)
    menu()

def kalendarz():
    import calendar
    yy = int(input("Podaj rok"))
    mm = int(input("Podaj miesiac"))
    print('  Python Calendar\n ')
    print(calendar.month(yy,mm))
    menu()
 
def zgadnij_liczbe():
    print("Podaj liczbe")
    liczba = int(input())
    import random
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

def quiz_matematyczny():
    print("Witam w quizie")
    wynik = 0
    import random
    i=0
    while(i<5):
        print("Odpowiedz na moje pytanie:")
        liczba1 = int(random.randint(1, 10))
        liczba2 = int(random.randint(1, 10))
        print(liczba1 ," + ",liczba2," = ?")
        liczba = int(input())
        i += 1
        if (liczba == liczba1 + liczba2):
            wynik += 1
            print("Brawo!")
    print("Twój wynik, to: ",wynik)
    menu()

def zgadnij_kolor():
    import random
    print("My colors: red, blue, cyan, pink, green")
    print("Please pick one from these color, we will see if you'll get the same choice as me!")
    color = random.choice(["red", "blue", "cyan", "pink", "green"])
    choose = input()
    while(choose != color):
        print("Bad colour")
        if(color == "red"):
            print("You are quite RED right now?")
            choose = input()
        elif (color == "blue"):
            print("You are quite BLUE right now?")
            choose = input()
        elif (color == "cyan"):
            print("You are quite CYAN right now?")
            choose = input()
        elif (color == "pink"):
            print("You are quite PINK right now?")
            choose = input()
        elif (color == "green"):
            print("You are quite GREEN right now?")
            choose = input()
    if(choose == color):
        print("Well done!")
    menu()

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

"""
#71

sporty = ['koszykówka', 'rower']
print(sporty)
print("Podaj mi swój ulubiony sport, którego nie ma na liście.")
sporty += (input(),)
print('Uaktualniona wysortowana, lista, to: ')
sporty.sort()
print(sporty)

#72
przedmioty = ["fizyka", "matematyka", "wf", "plastyka", "informatyka", "polski"]
print(przedmioty)
print("Którego przedmiotu nie lubisz?")
przedmioty.remove(input())
print("Twój nowy plan lekcji:), to: ")
print(przedmioty)

"""
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

"""
from array import *

numery = array ('i',[11, 22, 33, 44, 55])
print(numery)
print("Wybierz numer, a ja podam ci jego indeks.")
wybor = int(input("Wpisz liczbę: "))
while(wybor not in numery):
    print("Tej liczby nie mam w moim arrayu, wpisz prawidłową liczbę!")
    wybor = int(input("Wpisz liczbę kolejną liczbę: "))

print(numery.index(wybor))

#95
from array import *
numery = array("d", [55.55, 66.66, 77.77, 88.88, 99.99])
print(numery)
while(input("Podaj liczbę od 2 do 5") < 2 or input("Podaj liczbę od 2 do 5") > 5):
    print("test")
    nie jest skonczone :(

#Zadania na plikach
file = open("Countries.txt", "w")
file.write("Italy\n")
file.write("Germany\n")
file.write("Spain\n")
file.close

file = open("Countries.txt", "r")
print(file.read())

file = open("Countries.txt", "a")
file.write("France\n")
file.close

#106

file = open("Names.txt", "w")
file.write("Andrzej\n")
file.write("Mariusz\n")
file.write("Patryk\n")
file.write("Magda\n")
file.write("Karolina\n")
file.close


#107
file = open("Names.txt", "r")
print(file.read())

#108
file = open("Names.txt", "a")
print("Wpisz jakies imie, a ja je dopisze do pliku!")
file.write(input())
file.write("\n")
file.close()
file = open("Names.txt", "r")
print(file.read())
file.close()

#105
file = open("Numbers.txt", "w")
file.write("1,")
file.write("2,")
file.write("3,")
file.write("4,")
file.write("5")
file.close()


#CSV
file = open("Stars.csv", "w")
newRecord = "Brian,73,taurus\n"
file.write(str(newRecord))
file.close()

#CSV1
file = open("Stars.csv", "a")
name = input("Enter name: ")
age = input("Enter age: ")
star = input("Enter star sign: ")
newRecord = name + "," + age + "," + star + "\n"
file.write(str(newRecord))
file.close()


#111
file = open("Books.csv", "w")
newRecord = "To kill,Harper,1960\n"
newRecord1 = "A brief,Stephen,1988\n"
newRecord2 = "The great Gatsby,F.Scott,1922\n"
file.write(str(newRecord))
file.write(str(newRecord1))
file.write(str(newRecord2))
file.close()


#112
file = open("Books.csv", "a")
name = input("Enter book: ")
author = input("Enter Author: ")
year = input("Enter Year Released: ")
newRecord = name + "," + author + "," + year + "\n"
file.write(str(newRecord))
file.close()


#113
i = int(input("Ile chcesz dodać rekorkdów?"))
while (i > 0):
    file = open("Books.csv", "a")
    name = input("Enter book: ")
    author = input("Enter Author: ")
    year = input("Enter Year Released: ")
    newRecord = name + "," + author + "," + year + "\n"
    file.write(str(newRecord))
    file.close()
    i = i - 1



wybor_funckji()

"""
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


def tabliczka_mnozenia_wybranej_liczby():
    num = int(input("Podaj liczbe, a ja wyswietle tabliczke mnozenia "))
    i = int(1)
    while i < 11:
        print(num, 'x', i, '=', num*i)
        i+=1
    menu()

def liczba_na_rozne_systemy_liczbowe():

    liczba = input("Wpisz liczbę.")

    print("Liczba ", liczba, " to inaczej:")
    print(bin(liczba), "w systemie dwojkowym.")
    print(oct(liczba), "w systemie osemkowym.")
    print(hex(liczba), "w systemie szesnastkowym.")

    menu()





def menu():
    print('''
        1Lista dostępnych programow:
        1.dodawanie
        2.odejmowanie
        3.mnozenie
        4.dzielenie całkowite bez reszty
        5.modulo, reszta z dzielenia
        6.dzielenie_z_reszta
        7.potegowanie
        8.kalendarz
        9.zgadnij_liczbe
        10.quiz_matematyczny
        11.zgadnij_kolor
        12.tuple_indexy
        13.lista_zaproszonych
        14.wyraz_w_pionie

    ''')



    lang = input("Wbyierz program z powyzszych \n")

    match lang:
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
            quiz_matematyczny()
        case "11":	
            zgadnij_kolor()
        case "12":	
            tuple_indexy()
        case "13":	
            lista_zaproszonych()
        case "14":	
            wyraz_w_pionie()
        case "15":	
            znajdz_najwieksza_liczbe()
        case "16":	
            tabliczka_mnozenia_wybranej_liczby()
        case "17":	
            liczba_na_rozne_systemy_liczbowe()

        case _:
            print("Proszę wpisz dobry numer.")
            menu()

menu()