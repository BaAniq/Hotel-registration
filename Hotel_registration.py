from prettytable import PrettyTable
table = PrettyTable()
table_rooms = PrettyTable()


with open('Guest List', 'a+', encoding="UTF-8") as Guest_List_file:
    Guest_List_file.seek(0)


options = (1, 2, 3, 4, 5)
rooms = ('111', '112', '121', '122', '211', '212', '221', '222')
rooms_status = {
        '1 F': {
            '1 bed': {
                '111': 'available',
                '112': 'available',
                    },
            '2 bed': {
                '121': 'available',
                '122': 'available',
                    },
                },
        '2 F': {
            '1 bed': {
                '211': 'available',
                '212': 'available',
                    },
            '2 bed': {
                '221': 'available',
                '222': 'available',
                    },

                },
        }


def menu():
    choice = int(input('What do you want to do?:\
                \n  1 - show the Guest List\
                \n  2 - check in guest \
                \n  3 - check out guest \
                \n  4 - edit data \
                \n  5 - show room status \n'))
    return choice


def print_guests():
    table.field_names = ['Num', 'Name', 'Last name', 'Room']
    table.clear_rows()
    list_from_file = convert_file_to_list()
    num = 1
    for name, last_name, room in list_from_file:
        table.add_row([num, name, last_name, room])
        num += 1
    print(table)


def check_in():
    with open('Guest List', 'a+', encoding="UTF-8") as Guest_List_file:
        name = (input('Name:   ')+' ').capitalize()
        last_name = (input('Last name:   ')+' ').capitalize()
        room = (input('Room: '))
        if room not in rooms:
            while room not in rooms:
                print(f'No such room as {room} Try again')
                room = (input('Room: '))
        room = room + '\n'
        new_guest = [name, last_name, room]
        for data in new_guest:
            Guest_List_file.write(data)


def check_out():
    guest_list_from_file = convert_file_to_list()
    print_guests()
    guest_to_check_out = int(input('Which guest would you like to check out?: ')) - 1
    guest_list_from_file.pop(guest_to_check_out)
    updated_guest_list_to_file(guest_list_from_file)


def edition():
    guest_list_from_file = convert_file_to_list()
    print_guests()
    guest_to_edit = int(input('Which guest data would you like to edit?: ')) - 1
    num = 1
    for data in guest_list_from_file[guest_to_edit]:
        print(num, '. ', data)
        num += 1
    data_to_edit = int(input('Which data would you like to edit?: ')) - 1
    new_data = input('New value: ')
    guest_list_from_file[guest_to_edit][data_to_edit] = new_data
    updated_guest_list_to_file(guest_list_from_file)
    print_guests()


def convert_file_to_list():
    with open('Guest List', 'a+', encoding='UTF-8') as Guest_List_file:
        Guest_List_file.seek(0)
        guest_list_from_file = []
        for guest in Guest_List_file:
            guest_list_from_file.append(guest)
    for guest in guest_list_from_file:
        index = guest_list_from_file.index(guest)
        guest = guest.split()
        guest_list_from_file[index] = guest
    return guest_list_from_file


def updated_guest_list_to_file(guest_list_from_file):
    with open('Guest List', 'w+', encoding='UTF-8') as Guest_List_file:
        for guest in guest_list_from_file:
            guest = ' '.join(guest)
            Guest_List_file.write(guest)
            Guest_List_file.write('\n')

def show_room_status():
    table_rooms.field_names = ['Num', 'Beds', 'Floor', 'Room', 'Status']
    table_rooms.clear_rows()
    num = 1

    for floor in rooms_status:
        for bed in rooms_status[floor]:
            for num_room in rooms_status[floor][bed]:
                status = rooms_status[floor][bed][num_room]
                table_rooms.add_row([num, bed, floor, num_room, status])
                num += 1
    print(table_rooms)


z = 1
options_to_continue = (0, 1)
while z == 1:
    user_choice = menu()
    if user_choice in options:
        if user_choice == 1:
            print_guests()
        elif user_choice == 2:
            check_in()
        elif user_choice == 3:
            check_out()
        elif user_choice == 4:
            edition()
        elif user_choice == 5:
            show_room_status()
    else:
        print('Wrong choice. Please try again.')
        continue
    z = int(input('Do you want to continue:    \
            \n 1 - Yes\
            \n 0 - No \n '))
    if z not in options_to_continue:
        while z not in options_to_continue:
            print('Wrong choice. Try again')
            z = int(input('Do you want to continue:    \
                    \n 1 - Yes\
                    \n 0 - No \n '))
