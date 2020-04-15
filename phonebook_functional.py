import datetime as dt
import sqlite3 as sql


def __phone_check__(string):
    if '+7' in string:
        arr = list(string)
        arr.pop(0)
        arr.pop(0)
        arr.insert(0, '8')
        return ''.join(arr)
    return string


def __date_check__(date):
    if date:
        day, month, year = int(date[0:2]), int(date[3:5]), int(date[6:10])
        if day and month and year:
            birthdate = None
            while not birthdate:
                try:
                    birthdate = dt.date(year, month, day)
                except:
                    date = input('Enter correct date\n')
                    day, month, year = int(date[0:2]), int(date[3:5]), int(date[6:10])
        return date
    else:
        return '0'


def __id_input__():
    print('Enter name and surname or 0 if you want to exit')
    inp = ' '.join(input().split())
    if inp == '0':
        print('Exiting...')
        return '', ''
    while True:
        try:
            name, surname = inp.split(' ')
            inp = ''
            break
        except:
            inp = ' '.join(input('Enter both name and surname, please\n').split())
    if not __is_exists__(name, surname):
        print('no such record')
        return '', ''
    return name.capitalize(), surname.capitalize()


def __is_exists__(name, surname):
    name, surname = name.capitalize(), surname.capitalize()
    sql_op = """SELECT * FROM phonebook WHERE name='{}' AND surname='{}'""".format(name, surname)
    cursor.execute(sql_op)
    if cursor.fetchall():
        return True
    return False


def print_book():
    cursor.execute('SELECT * FROM phonebook ORDER BY name')
    data = cursor.fetchall()
    print('=====================')
    for tup in data:
        [print(elem, '\t', end = ' ') for elem in tup if elem != '0']
        print()
    print('=====================')


def __add_person__(name = '', surname = '', phone = '', date = ''):
    name, surname = name.capitalize(), surname.capitalize()
    phone = __phone_check__(phone)
    date = __date_check__(date)
    sql_op = """INSERT INTO phonebook (name, surname, phone, date) VALUES ('{}', '{}', '{}', '{}')""" \
        .format(name, surname, phone, date)
    cursor.execute(sql_op)
    conn.commit()


def add_person():
    print('Enter name and surname or 0 if you want to exit this function',
          'Example - Ivan Ivanov'
          , sep = '\n')
    inp = ' '.join(input().split())  # for trimming and removing extra whitespaces
    if inp == '0':
        print('Exiting...')
        return
    while True:
        try:
            name, surname = inp.split(' ')
            break
        except:
            inp = ' '.join(input('Enter both name and surname, please\n').split())
    if __is_exists__(name, surname):
        print('This person is already in list.', 'Would you like to change existing record',
              'Y - change', 'N - return to command choice', sep = '\n')
        answ = input().capitalize()
        while answ != 'Y' and answ != 'N':
            answ = input("Please, enter on of these two options - Y or N\n").capitalize()
        if answ == 'Y':
            chane_field(name, surname)
        return
    print('Enter phone number')
    phone = input().strip()
    print('Enter birthdate or 0 if you do not want to fill this field',
          'Date should be in format %DD.%MM.%YYYY',
          sep = '\n')
    date = input().strip()
    if date == '0':
        date = ''
    __add_person__(name, surname, phone, date)
    print('Added')



def __delete_person__(name = '', surname = '', phone = '', date = ''):
    if name and surname:
        name, surname = name.capitalize(), surname.capitalize()
        sql_op = '''SELECT * FROM phonebook WHERE name = "{}" AND surname = "{}"'''.format(name, surname)
        mess1, mess2 = 'No records with these name and surname', ''
    elif phone:
        sql_op = '''SELECT * FROM phonebook WHERE phone = "{}"'''.format(phone)
        mess1, mess2 = 'No records with this phone', 'There are several records with this phone'
    elif date:
        sql_op = '''SELECT * FROM phonebook WHERE date = "{}"'''.format(date)
        mess1, mess2 = 'No records with this birthdate', 'There are several records with this birthdate'
    else:
        return
    cursor.execute(sql_op)
    records = cursor.fetchall()
    if not records:
        print(mess1)
        return
    elif len(records) == 1:
        sql_op = '''DELETE FROM phonebook WHERE name = "{}" AND surname = "{}"'''.format(name, surname)
        cursor.execute(sql_op)
    elif len(records) > 1:
        print(mess2)
        print('=====================')
        for tup in records:
            [print(elem, end = ' ') for elem in tup]
            print()
        print('=====================')
        print('Type in name and surname that you want to delete')
        name, surname = __id_input__()
        sql_op = '''DELETE FROM phonebook WHERE name = "{}" AND surname = "{}"'''.format(name, surname)
        cursor.execute(sql_op)
    conn.commit()


def delete_person():
    print('Enter name and surname or phone number or 0 is you want to exit')
    inp = ' '.join(input().split())
    if inp == '0':
        print('Exiting...')
        return
    if not ('+7' in inp or '8' in inp) and not '.' in inp:
        while True:
            try:
                name, surname = inp.split(' ')
                inp = ''
                break
            except:
                inp = ' '.join(input('Enter both name and surname, please\n').split())
        if not __is_exists__(name, surname):
            print('no such record')
            return
        __delete_person__(name = name, surname = surname)
        print('Deleted')
    elif '.' in inp:
        inp = __date_check__(inp)
        __delete_person__(date = inp)
        print('Deleted')
    else:
        inp = __phone_check__(inp)
        __delete_person__(phone = inp)
        print('Deleted')

def __change_field__(field, data, name, surname):
    if field == 'date':
        data = __date_check__(data)
    elif field == 'name' or field == 'surname':
        data = data.capitalize()
    elif field == 'phone':
        data = __phone_check__(data)

    sql_op = '''UPDATE phonebook SET {} = "{}" WHERE name = "{}" AND surname = "{}"'''.format(field, data,
                                                                                              name, surname)
    cursor.execute(sql_op)
    conn.commit()


def chane_field(name = '', surname = ''):
    if not (name and surname):
        name, surname = __id_input__()
        if not (name and surname):
            return

    print('What field do you want to change?',
          'name, surname, phone, date',
          sep = '\n')
    field = input().strip()
    print('Enter new value for this field')
    val = input().strip()
    __change_field__(field, val, name, surname)
    print("Changing complete")


def __age_output__(name, surname):
    name, surname = name.capitalize(), surname.capitalize()
    sql_op = '''SELECT date FROM phonebook WHERE name = "{}" AND surname = "{}"'''.format(name, surname)
    cursor.execute(sql_op)
    date = list(cursor.fetchall())
    date = date[0][0]
    # birthdate = dt.datetime.strptime(data[0][0], '%d.%m.%y')
    day, month, year = int(date[0:2]), int(date[3:5]), int(date[6:10])
    birthdate = dt.date(year, month, day)
    curr_data = dt.datetime.now()
    from dateutil.relativedelta import relativedelta
    difference_in_years = relativedelta(curr_data, birthdate).years
    return difference_in_years


def age_output():
    name, surname = __id_input__()
    if not (name and surname):
        return
    print(name, surname, 'is now', __age_output__(name, surname), 'years old')


def search():
    inp = ' '.join(input('Enter what you want to search for\n'
                         'Name, surname, phone number or birthdate\n'
                         'Or enter 0 if you want to exit').split())
    if inp == '0':
        print('Exiting...')
        return
    elif ('+7' in inp or inp[0] == '8') and '.' not in inp:
        inp = __phone_check__(inp)
    elif '.' in inp:
        inp = __date_check__(inp)
    else:
        inp = inp.capitalize()
    sql_op = '''SELECT * FROM phonebook WHERE name = "{}" OR surname = "{}" OR phone = "{}" OR date = "{}"''' \
        .format(inp, inp, inp, inp)
    cursor.execute(sql_op)
    data = cursor.fetchall()
    if not data:
        print('No matches')
        return
    print('=====================')
    for tup in data:
        [print(elem, end = ' ') for elem in tup if elem != '0']
        print()
    print('=====================')


conn = sql.connect('phonebook.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook
                                (name text, surname text, phone text, date text)''')

# __add_person__('Dmitriy', 'Medvedev', '89340007579', '')
# __change_field__('name', 'Anatoliy', 'Dmitriy', 'Medvedev')
# fetched_name = cursor.execute('''SELECT name FROM phonebook WHERE name = "Anatoliy" and surname = "Medvedev"''').fetchall()
# print(fetched_name)
# __delete_person__('Anatoliy', 'Medvedev')
# # print_book()