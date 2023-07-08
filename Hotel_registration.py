# TYPY ZAGNIEŻDŻONE

osoba1=[217,'Orlando','Bloom',25,'mężczyzna']
osoba2=[217,'Katy','Perry',25,'kobieta']
osoba3=[218,'Angelina','Jolie',51,'kobieta']
osoba4=[218,'Brad','Pitt',46,'mężczyzna']
osoba5=[117,'Henryk','Sienkiewicz',18,'mężczyzna']

listaG=[osoba1,osoba2,osoba3,osoba4,osoba5]


z=1
# dodawanie gości
while z==1:
    wybor=int(input('Co chcesz zrobić:\
            \n  1 - wyświetlić listę gości\
            \n  2 - zameldować gości\
            \n  3 - wymeldować gości \n'))


    if wybor==1:
          for d in listaG:
              print(d)
    elif wybor==2:
        imie=input('Imię:   ')
        imie=imie.capitalize()
        nazw=input('Nazwisko:   ')
        nazw=nazw.capitalize()
        wiek=int(input('Wiek:   '))
        plec=input('Płeć:   ')
        pokoj=int(input('Pokój: '))
        gosc=[pokoj,imie,nazw,wiek,plec]
        listaG.append(gosc)
        
    elif wybor==3:
        x=0
        for i in range(1,len(listaG)+1):
        
            print(f'{i}.',listaG[x])
            
            x+=1
        gusu=int(input('Którego gościa chcesz wymeldować?:  '))
        r=gusu-1
        listaG.pop(r)

    z=int(input('Czy chcesz kontynuować:    \
            \n 1 - Tak\
            \n 2 - Nie \n '))
