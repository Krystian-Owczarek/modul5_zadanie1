from faker import Faker
fake = Faker()


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email}'


class BusinessContact(BaseContact):
    def __init__(self, job_title, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company = company
        self.business_phone = business_phone

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email} {self.job_title} {self.company} {self.business_phone}'


def create_contacts(type, value):

    for i in range(value):
        random_person = BaseContact(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), email=fake.ascii_email())

        if type == 1:
            print(random_person)

        elif type == 2:
            random_person = BusinessContact(random_person, job_title=fake.job(), company=fake.company(), business_phone=fake.phone_number())
            print(random_person)
        else:
            print('Choose 1 if you want to create Base Contact or 2 if you want to create Business Contact')

create_contacts(1,10)
    


