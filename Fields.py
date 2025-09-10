from datetime import datetime, date, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isnumeric():
            super().__init__(value)
        else:
            raise Exception("Phone number must be 10 digits and all numeric")


class Birthday(Field):
    def __init__(self, value):
        value = datetime.strptime(value, "%d.%m.%Y").date()
        super().__init__(value)


    def __str__(self):
        return self.value.strftime("%d.%m.%Y")