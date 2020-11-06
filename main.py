class Directory:
    def __init__(self):
        self.entries = list()

    def add_entry(self, new_entry):
        if len(self.find_entry(new_entry.email)) > 0:
            print("Данный элемент уже существует")
        else:
            self.entries.append(new_entry)

    def find_entry(self, field_value):
        founded_entries = list()
        for entry_in_directory in self.entries:
            for field in vars(entry_in_directory):
                if field_value == field:
                    break
            else:
                continue
            founded_entries.append(entry_in_directory)
        return founded_entries

    def delete_entry(self, entry_to_delete):
        self.entries.remove(entry_to_delete)


class Entry:
    def __init__(self, name, surname, telephone, city, email):
        if not (self.check_text_fields(name) and self.check_text_fields(
                surname) and self.check_telephone(
                telephone) and self.check_text_fields(
                city) and self.validate_email(email)):
            print("Некорректные значения полей")
            return
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.city = city
        self.email = email

    @staticmethod
    def check_text_fields(field_value):
        for sym in str(field_value):
            if not sym.isalpha():
                return False
        else:
            return True

    @staticmethod
    def check_telephone(number):
        if str(number).isdigit():
            return True
        else:
            return False

    @staticmethod
    def validate_email(email):
        hasAt = False
        for symbol in email:
            if symbol == '@':
                hasAt = True
            elif symbol == '.' and hasAt:
                return True
        return False

    def set_name(self, value):
        if self.check_text_fields(value):
            self.name = value
        else:
            print("Введено некоректное значение")

    def set_surname(self, value):
        if self.check_text_fields(value):
            self.surname = value
        else:
            print("Введено некоректное значение")

    def set_telephone(self, value):
        if self.check_telephone(value):
            self.telephone = value
        else:
            print("Введено некоректное значение")

    def set_city(self, value):
        if self.check_text_fields(value):
            self.city = value
        else:
            print("Введено некоректное значение")

    def set_email(self, value):
        if self.validate_email(value):
            self.email = value
        else:
            print("Введено некоректное значение")
