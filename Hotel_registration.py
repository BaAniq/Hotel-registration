def menu():
    choice = int(input('What do you want to do?:\
                \n  1 - show the Guest List\
                \n  2 - check in guest \
                \n  3 - check out guest \
                \n  4 - edit data \n'))
    return choice


def print_guest_list():
    with open('Guest List', 'a+', encoding="UTF-8") as Guest_List:
        Guest_List.seek(0)
        print(Guest_List.read())


def check_in():
    with open('Guest List', 'a+', encoding="UTF-8") as Guest_List:
        name = (input('Name:   '))+' '
        name = name.capitalize()
        Guest_List.write(name)

        surname = input('Surname:   ')+' '
        surname = surname.capitalize()
        Guest_List.write(surname)

        age = input('Age:   ')+' '
        Guest_List.write(age)

        room = input('Room: ')+'\n'
        Guest_List.write(room)


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
