from colorama import Fore, Style
from AddressBook import *

"""Декоратор для обробки помилок"""
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return Fore.RED + str(e) + Style.RESET_ALL
    return inner

"""Функція інпуту"""
@input_error
def user_input(mes_to_user):
    first_param, *args = input(mes_to_user).split()
    first_param = first_param.lower()
    return first_param, *args

"""Просте вітання з користувачем і одразу опис функції help"""
@input_error
def greeting(*args):
    if args:
        raise Exception('Do not need params')
    return Fore.YELLOW + "Hi! I`m a simple bot which works with phone numbers.\n    " + Style.RESET_ALL + "You can have some help: write 'help'"

"""Опис всіх команд"""
@input_error
def help_command(*args):
    if args:
        raise Exception('Do not need params')
    help_message = Fore.YELLOW + "Use next commands:\n" + Style.RESET_ALL + \
            "    'add' to add a number or contact(add [name] [(not required) number])\n\
    'change' to change number (change [name] [old number] [new number])\n\
    'contact' to get a contact info (phone [name])\n\
    'remove' to remove a contact or number (remove [name] [(not required) number])\n\
    'all' to get all contacts info (all)\n\
    'add-birthday' to add birthday to contact (add-birthday [name] [birthday (dd.mm.yyyy)]\n\
    'show-birthday' to show contact birthday (show-birthday [name])\n\
    'birthdays' to show all birthday in near 7 days (birthdays)\n\
    'close' or 'exit' or 'quit' to exit the bot (close) or (exit) or (quit)"
    return help_message


"""Функція для відображення контакту"""
@input_error
def get_contact(*args):
    if len(args) == 1:
        contact = addressbook.find(args[0])
        if contact:
            contact_str = f'--------------------\nContact name: {contact.name}, phones: '
            if contact.phones:
                return contact_str + str(' ;'.join(map(str, contact.phones))) + ';\n--------------------'
            return contact_str + ';\n--------------------'
        raise Exception('Contact not found')
    raise Exception('Only one parameter is allowed')

"""Функція для відображення всіх контактів"""
@input_error
def get_all_phones(*args):
    if args:
        raise Exception('Do not need params')
    elif addressbook:
        return str(addressbook)
    else:
        raise Exception('No contacts exists')


"""Функція, що додає новий контакт, або додає новий номер якщо контакт вже існує"""
@input_error
def add_contact(*args):
    # global addressbook
    if not len(args) in [1, 2]:
        raise Exception('Waiting for one or two params({Contact name}, {Phone}).')
    elif len(args) == 2:
        number = args[1]
    else:
        number = None
    name = args[0]
    if not addressbook.find(name):
        new_record = Record(name)
        if number:
            new_record.add_phone(number)
        addressbook.add_record(new_record)
        return Fore.YELLOW + 'Contact created successfully'
    elif number:
        addressbook[name].add_phone(number)
        return Fore.YELLOW + 'Number successfully added to contact.' + Style.RESET_ALL
    return Fore.RED + 'Contact with this name already exists'


"""Функція яка замінює номер з контакту на новий доданий"""
@input_error
def change_phone(*args):
    if (len(args)) != 3:
        raise Exception('Waiting for three params({Contact name}, {Old phone}, {New phone}).')
    else:
        name, old_phone, new_phone = args
        addressbook[name].edit_phone(old_phone, new_phone)
        return Fore.YELLOW + 'Contact changed successfully.' + Style.RESET_ALL


"""Функція, що видаляє контакт з адресної книги, або тільки номер з контакту"""
@input_error
def remove_contact(*args):
    if len(args) not in [1, 2]:
        raise Exception('Waiting for one or two params({Contact name}, {Phone}).')
    elif len(args) == 2:
        number = args[1]
        addressbook[args[0]].remove_phone(number)
        return Fore.YELLOW + 'Contact number removed successfully.' + Style.RESET_ALL
    addressbook.delete(args[0])
    return Fore.YELLOW + 'Contact removed successfully.' + Style.RESET_ALL


"""Функція, що додає день народження до існуючого контакту"""
@input_error
def add_birthday(*args):
    if len(args) != 2:
        raise Exception('Waiting for two params({Contact name}, {Birthday}).')
    name, birthday = args
    birth_contact = addressbook.find(name)
    if birth_contact:
        birth_contact.add_birthday(birthday)
        return Fore.YELLOW + 'Birthday added successfully.' + Style.RESET_ALL
    return Fore.RED + 'Contact not found.' + Style.RESET_ALL


"""Функція що відображає контакт і його день народження"""
@input_error
def show_birthday(*args):
    if len(args) != 1:
        raise Exception('Waiting for one param {Contact name}.')
    name = args[0]
    birth_contact = addressbook.find(name)
    if birth_contact:
        if birth_contact.birthday:
            return f'--------------------\nName: {birth_contact.name}, Birthday: {birth_contact.birthday}\n--------------------'
        raise Exception('Birthday not found for this contact')
    raise Exception('Contact not found')

"""Функція, що відображає всі контакти, в яких день народження буде за найближчі 7 днів"""
@input_error
def birthdays():
    birthdays_list = addressbook.get_upcoming_birthdays()
    if birthdays:
        birth_str = '--------------------\n'
        for elem in birthdays_list:
            birth_str += f'Contact name: {elem.name}, birthday: {elem.birthday}\n'
        return birth_str + '--------------------'
    raise Exception('No birthdays found')


def main():
    print(Fore.BLUE + 'Welcome to my first bot!' + Style.RESET_ALL)
    while True:
        first_param, *args = user_input(Fore.BLUE + 'Enter a command: ' + Style.RESET_ALL)
        match first_param.lower():
            case 'hello':
                print(greeting(*args))
            case 'help':
                print(help_command(*args))
            case 'add':
                print(add_contact(*args))
            case 'change':
                print(change_phone(*args))
            case 'contact':
                print(get_contact(*args))
            case 'remove':
                print(remove_contact(*args))
            case 'all':
                print(get_all_phones(*args))
            case 'add-birthday':
                print(add_birthday(*args))
            case 'show-birthday':
                print(show_birthday(*args))
            case 'birthdays':
                print(birthdays(*args))
            case 'close' | 'exit' | 'quit':
                print(Fore.YELLOW + 'Goodbye!' + Style.RESET_ALL)
                break
            case _:
                print(Fore.RED + "Invalid command. Print 'help' for have some help" + Style.RESET_ALL)

if __name__ == '__main__':
    addressbook = AddressBook()
    main()
