from phonebook_functional import *


comm = 1
while comm:
    print('Choose one of the commands',
          'add - Add new record to the phonebook',
          'delete - Delete existing record to the phonebook',
          'change - Change some field in existing record',
          'print all - Print all phonebook',
          'print age - Print a certain person\'s age',
          'search - Search for something in whole phonebook',
          '0 - Exit',
          sep = '\n')
    comm = (' '.join(input().split()).capitalize())

    if comm == '0' or comm == 'Exit':
        break

    elif comm == 'Add':
        add_person()

    elif comm == 'Delete':
        delete_person()

    elif comm == 'Change':
        chane_field()

    elif comm == 'Print all':
        print_book()

    elif comm == 'Print age':
        age_output()

    elif comm == 'Search':
        search()

    else:
        print('No such command')
    # print('\n')
