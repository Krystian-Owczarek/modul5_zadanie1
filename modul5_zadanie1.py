from faker import Faker
fake = Faker()

import logging
logging.basicConfig(level=logging.INFO)


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

        #Values
        self._label_length = 0

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email}'

    def contact(self):
        print(f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}')

    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = len(self.name) + len(self.surname)


class BusinessContact(BaseContact):
    def __init__(self, job_title, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company = company
        self.business_phone = business_phone

        #Values
        self._label_length = 0

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email} {self.job_title} {self.company} {self.business_phone}'

    def contact(self):
        print(f'Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.surname}')

    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = len(self.name) + len(self.surname)


def create_contacts(type, value):

    for i in range(value):
        random_person = BaseContact(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), email=fake.ascii_email())

        if type == 1:
            print(random_person)
            random_person.contact()
            random_person.label_length = 0 #Nie wiem dlaczego, ale bez tego ponownego przypisania wartości, random_person.label_length zwraca mi wartość bazową (0), tak jakby olewał @label_lenght.setter
            print(f'Długość imienia i nazwiska to: {random_person.label_length}')

        elif type == 2:
            random_person = BusinessContact(name=random_person.name, surname=random_person.surname, phone=random_person.phone, email=random_person.email, job_title=fake.job(), company=fake.company(), business_phone=fake.phone_number())
            print(random_person)
            random_person.contact()
            random_person.label_length = 0 #Nie wiem dlaczego, ale bez tego ponownego przypisania wartości, random_person.label_length zwraca mi wartość bazową (0), tak jakby olewał @label_lenght.setter
            print(f'Długość imienia i nazwiska to: {random_person.label_length}')
        else:
            print('Wybór nie jest liczbą od 1 do 2, spróbuj ponownie: \n1 Prywatna, \n2 Biznesowa, \n3 Wyjdź')


if __name__ == "__main__":
    
    while True:
        print('Wybierz rodzaj wizytówki 1-prywatna 2-biznesowa (lub wpisz 3 aby wyjść), a następnie podaj ilość którą chcesz wygenerować')

        while True:
            try:
                choice_number = int(input('Opcja '))\

                if choice_number <= 2:
                    break;
                elif choice_number == 3:
                    exit()
                else:
                     logging.warning('Wybór nie jest liczbą od 1 do 2, spróbuj ponownie: \n1 Prywatna, \n2 Biznesowa, \n3 Wyjdź')

            except ValueError:
                logging.warning('Wybór nie jest liczbą od 1 do 2, spróbuj ponownie: \n1 Prywatna, \n2 Biznesowa, \n3 Wyjdź')

        while True:
            try:
                number_of_cards = int(input('Podaj ilość: '))
                break;

            except ValueError:
                logging.warning('Wybór nie jest liczbą całkowitą, spróbuj ponownie')

        create_contacts(choice_number, number_of_cards)