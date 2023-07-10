guest1 = ['217', 'Orlando', 'Bloom', '25', 'man']
guest2 = ['217', 'Katy', 'Perry', '25', 'woman']
guest3 = ['218', 'Angelina', 'Jolie', '51', 'woman']
guest4 = ['218', 'Brad', 'Pitt', '46', 'man']
guest5 = ['117', 'Henryk', 'Sienkiewicz', '18', 'man']

list_guest = [guest1, guest2, guest3, guest4, guest5]


def menu():
    choice = int(input('What do you want to do?:\
                \n  1 - show the Guest List\
                \n  2 - check in guest \
                \n  3 - check out guest \
                \n  4 - edit data \n'))
    return choice


def print_guest_list():
    l = 1
    for guest in list_guest:
        print(l, guest)
        l += 1


def check_in():
    name = input('Name:   ')
    name = name.capitalize()
    surname = input('Surname:   ')
    surname = surname.capitalize()
    age = int(input('Age:   '))
    sex = input('Sex:   ')
    room = int(input('Room: '))
    guest = [room, name, surname, age, sex]
    list_guest.append(guest)


def check_out():
    x = 0
    for i in range(1, len(list_guest) + 1):
        print(f'{i}.', list_guest[x])
        x += 1
    guest_del = int(input('Which guest would you like to check out?:  ')) - 1
    list_guest.pop(guest_del)


def edition():
    print_guest_list()
    guest_to_edit_index = int(input('Which guest data would you like to edit?: '))-1
    guest_to_edit = [list_guest[guest_to_edit_index]]
    for room, name, surname, age, sex in guest_to_edit:
        print('1. Room: ', room)
        print('2. Name: ', name)
        print('3. Surname: ', surname)
        print('4. Age: ', age)
        print('5. Sex: ', sex)
    data_to_edit = int(input('Which data would you like to edit?: '))-1
    new_value = input('New value: ')
    list_guest[guest_to_edit_index][data_to_edit] = new_value


z = 1

while z == 1:
    user_choice = menu()
    if user_choice == 1:
        print_guest_list()
    elif user_choice == 2:
        check_in()
    elif user_choice == 3:
        check_out()
    elif user_choice == 4:
        edition()
    z = int(input('Do you want to continue:    \
            \n 1 - Yes\
            \n 2 - No \n '))
