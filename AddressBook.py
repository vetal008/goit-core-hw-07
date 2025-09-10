
from collections import UserDict
from Record import *

class AddressBook(UserDict):
    """Додавання нового запису до книги"""

    def add_record(self, record: Record):
        if not self.find(record.name.value):
            self.data[record.name.value] = record
        else:
            raise ValueError('Contact with the same name already added')

    """Знаходження рекорду за ім'ям"""
    def find(self, name: str):
        return self.data.get(name)


    """Видалення рекорду"""
    def delete(self, name: str):
        if name in self.data.keys():
            del self.data[name]
        else:
            raise ValueError('Contact with the same name is not exist')


    def __str__(self):
        if self.data:
            address_str = '--------------------\n'
            for elem in self.data.values():
                address_str += (str(elem) + '\n')
            address_str += '--------------------'
            return address_str
        else:
            raise ValueError('Address book is empty')

    """Функція знаходження дня народження"""
    def find_birthday(self, name):
        for elem in self.data.values():
            if elem.name == name:
                return elem
        return None


    """Знаходження контактів у яких день народження за 7 днів"""
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for user in filter(lambda elem: elem.birthday, self.data.values()):
            birthday_this_year = user.birthday.value.replace(year=today.year)
            birthday_next_year = birthday_this_year.replace(year=today.year + 1)
            if 0 <= (birthday_next_year - today).days <= days:
                birthday_this_year = birthday_next_year
            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())
                upcoming_birthdays.append(user)
        if upcoming_birthdays:
            return upcoming_birthdays
        raise ValueError('No upcoming birthdays')
