# TYPY ZAGNIEŻDŻONE

guest1=[217, 'Orlando', 'Bloom', 25, 'mężczyzna']
guest2=[217, 'Katy', 'Perry', 25, 'kobieta']
guest3=[218, 'Angelina', 'Jolie', 51, 'kobieta']
guest4=[218, 'Brad', 'Pitt', 46, 'mężczyzna']
guest5=[117, 'Henryk', 'Sienkiewicz', 18, 'mężczyzna']

list_guest=[guest1, guest2, guest3, guest4, guest5]


z=1
# dodawanie gości
while z==1:
    choice=int(input('What do you want to do?:\
            \n  1 - show the Guest List\
            \n  2 - check in guest \
            \n  3 - check out guest \n'))


    if choice==1:
          for guest in list_guest:
              print(guest)
    elif choice==2:
        name=input('Name:   ')
        name=name.capitalize()
        surname=input('Surname:   ')
        surname=surname.capitalize()
        age=int(input('Age:   '))
        sex=input('Sex:   ')
        room=int(input('Room: '))
        guest=[room, name, surname, age, sex]
        list_guest.append(guest)
        
    elif choice==3:
        x=0
        for i in range(1, len(list_guest) + 1):
        
            print(f'{i}.', list_guest[x])
            
            x+=1
        guest_del=int(input('Which guest would you like to check out?:  '))-1

        list_guest.pop(guest_del)

    z=int(input('Do you want to continue:    \
            \n 1 - Yes\
            \n 2 - No \n '))
