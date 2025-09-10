from Fields import *

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    """Функція, що додає до рекорду день народження"""
    def add_birthday(self, birthday: str):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday already added")


    """Функція повертає номер з рекорду або нічого"""
    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p

    """Функція додає новий номер до рекорду"""
    def add_phone(self, phone: str):
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        else:
            raise ValueError('Phone already added')

    """Функція, що видаляє вказаний номер"""
    def remove_phone(self, phone: str):
        if self.find_phone(phone):
            self.phones.remove(self.find_phone(phone))
        else:
            raise ValueError('No such phone')

    """Функція, що змінює вказаний номер"""
    def edit_phone(self, phone: str, new_phone: str):
        if self.find_phone(phone):
            self.add_phone(new_phone)
            self.remove_phone(phone)
        else:
            raise ValueError('No such phone')


    def __str__(self):
        str_phones = '; '.join(p.value for p in self.phones) if self.phones else None
        return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {str_phones};"