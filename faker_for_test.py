from faker import Faker


def create_fullname(lastname, firstname, middlename):
    initial = middlename[0].upper() + "." if middlename else ""
    initial_name = firstname[0].upper() + "."
    full_name = lastname.capitalize() + " " + initial_name + " " + initial
    return full_name


def generate_fake_data_student(withPatronymic=True):
    faker = Faker("ru_RU")

    data = {
        "version": "string",
        "student": {
            "personalData": {
                "firstname": faker.first_name(),
                "lastname": faker.last_name(),
                "patronymic": faker.first_name() if withPatronymic else '',
                "lastnameInitials": "",
            }
        }
    }

    data["student"]["personalData"]["lastnameInitials"] = create_fullname(
        data["student"]["personalData"]["lastname"],
        data["student"]["personalData"]["firstname"],
        data["student"]["personalData"]["patronymic"],
    )

    if not withPatronymic:
        del data["student"]["personalData"]["patronymic"]

    return data

def format_phone_number(phone_number):
    phone_number = ''.join(filter(str.isdigit, phone_number))

    if phone_number.startswith('7') or phone_number.startswith('+7'):
        phone_number = '8' + phone_number[1:]

    return phone_number


def generate_fake_data_contacts(withEmail=True, withTelegram=True, withPhone=True):
    faker = Faker("ru_RU")

    fcontact = {
        "hasContact": True
    }

    if withEmail:
        fcontact["femail"] = {
            "hasEmal": True,
            "email": faker.email()
        }

    if withPhone:
        fcontact["fphone"] = {
            "hasPhone": True,
            "phone": format_phone_number(faker.phone_number())
        }

    if withTelegram:
        faker = Faker()
        fcontact["ftelegram"] = {
            "hasTelegram": True,
            "telegram": "@" + str(faker.user_name())
        }

    return fcontact

def generate_fake_data_git():
    faker = Faker()

    fgit = {
        "hasGit": True,
        "git": 'https://github.com/' + faker.user_name()
    }

    return fgit


print(generate_fake_data_student(False))
