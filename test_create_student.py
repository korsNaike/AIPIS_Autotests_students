import requests
import pytest
from faker import Faker
import datetime
from faker_for_test import *

BASE_URL = "http://192.168.0.16:8080/students/general"

def create_test_student():
    data = generate_fake_data_student()
    response = requests.post(url=BASE_URL, json=data)
    return response

def test_create_student():
    response = create_test_student()
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200
    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_create_student_without_patronymic():
    data = generate_fake_data_student(withPatronymic=False)
    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200
    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_create_student_with_contacts():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts()

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200

    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_create_student_with_email():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts(withPhone=False, withTelegram=False)

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200

    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_create_student_with_phone():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts(withEmail=False, withTelegram=False)

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200

    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_create_student_with_telegram():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts(withEmail=False, withPhone=False)

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200

    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_create_student_with_git():
    data = generate_fake_data_student()
    data["student"]["fgit"] = generate_fake_data_git()
    
    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200

    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_create_student_with_contacts_and_git():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts()
    data["student"]["fgit"] = generate_fake_data_git()
    
    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()
    student_id = response_body["info"][0]["id"]
    assert response.status_code == 200

    print(f"id созданного студента {student_id}")
    print("Время проведения теста: ", datetime.datetime.now())


def test_error_lastname():
    data = generate_fake_data_student(withPatronymic=False)
    data["student"]["personalData"]["lastname"] += '12412'

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid lastname format"

    print("Студент не был создан!")
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_firstname():
    data = generate_fake_data_student(withPatronymic=False)
    data["student"]["personalData"]["firstname"] += '12412'

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid firstname format"

    print("Студент не был создан!")
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_patronymic():
    data = generate_fake_data_student(withPatronymic=True)
    data["student"]["personalData"]["patronymic"] += '12412'

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid patronymic format"

    print("Студент не был создан!")
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_email():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts()
    data["student"]["fcontact"]["femail"]["email"] = "пустая строка"

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid email format"

    print("Студент не был создан!")
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_phone():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts()
    data["student"]["fcontact"]["fphone"]["phone"] = "пустая строка"

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid phone format"

    print("Студент не был создан!")
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_telegram():
    data = generate_fake_data_student()
    data["student"]["fcontact"] = generate_fake_data_contacts()
    data["student"]["fcontact"]["ftelegram"]["telegram"] = "пустая строка"

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid telegram format"

    print("Студент не был создан!")
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_git():
    data = generate_fake_data_student()
    data["student"]["fgit"] = generate_fake_data_git()
    data["student"]["fgit"]["git"] = "12313"

    response = requests.post(url=BASE_URL, json=data)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid git format"

    print("Студент не был создан!")
    print("Время проведения теста: ", datetime.datetime.now())


if __name__ == "__main__":
    pytest.main([__file__])