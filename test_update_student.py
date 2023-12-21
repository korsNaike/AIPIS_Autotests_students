import requests
import pytest
from faker import Faker
import datetime
from faker_for_test import *

BASE_URL = "http://192.168.0.16:8080/students/general"
URL_PUT_STUDENT = "http://192.168.0.16:8080/students/general/"

def create_test_student():
    data = generate_fake_data_student()
    response = requests.post(url=BASE_URL, json=data)
    return response


def test_update_student_with_contacts():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fcontact"] = generate_fake_data_contacts()

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 200

    print(f"Обновили студента с id={student_id}")
    print("Время проведения теста: ", datetime.datetime.now())



def test_update_student_with_email():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fcontact"] = generate_fake_data_contacts(withPhone=False, withTelegram=False)

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 200

    print(f"Обновили студента с id={student_id}")
    print("Время проведения теста: ", datetime.datetime.now())


def test_update_student_with_phone():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fcontact"] = generate_fake_data_contacts(withEmail=False, withTelegram=False)

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 200

    print(f"Обновили студента с id={student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_update_student_with_telegram():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fcontact"] = generate_fake_data_contacts(withPhone=False, withEmail=False)

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 200

    print(f"Обновили студента с id={student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_update_student_with_git():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fgit"] = generate_fake_data_git()

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 200

    print(f"Обновили студента с id={student_id}")
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_email():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fcontact"] = generate_fake_data_contacts(withPhone=False, withTelegram=False)
    data["student"]["fcontact"]["femail"]["email"] = "gasasdasd"

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid email format"

    print('Студент не был обновлен!')
    print("Время проведения теста: ", datetime.datetime.now())


def test_error_phone():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fcontact"] = generate_fake_data_contacts(withEmail=False, withTelegram=False)
    data["student"]["fcontact"]["fphone"]["phone"] = "gasasdasd"

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid phone format"

    print('Студент не был обновлен!')
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_telegram():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fcontact"] = generate_fake_data_contacts(withPhone=False, withEmail=False)
    data["student"]["fcontact"]["ftelegram"]["telegram"] = "-@!"

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid telegram format"

    print('Студент не был обновлен!')
    print("Время проведения теста: ", datetime.datetime.now())

def test_error_git():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fgit"] = generate_fake_data_git()
    data["student"]["fgit"]["git"] = "-@!"

    response = requests.put(url=URL_PUT_STUDENT + str(student_id), json=data)

    assert response.status_code == 202
    assert response_body["errorFields"][0]["message"] == "Invalid git format"

    print('Студент не был обновлен!')
    print("Время проведения теста: ", datetime.datetime.now())

def test_404_error():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    data = {
        "student": response_body["info"][0]
    }
    print(f"Создали студента с id={student_id}, пытаемся отправить PUT")

    data["student"]["fgit"] = generate_fake_data_git()

    response = requests.put(url=URL_PUT_STUDENT + "2000000000000000000000", json=data)

    assert response.status_code == 201

    print('Студент не был обновлен!')
    print("Время проведения теста: ", datetime.datetime.now())

