import requests
import pytest
from faker import Faker
import datetime
from faker_for_test import *

BASE_URL = "http://192.168.0.16:8080/students/general"

URL_GET_STUDENT = "http://192.168.0.16:8080/students/general/"

def create_test_student():
    data = generate_fake_data_student()
    response = requests.post(url=BASE_URL, json=data)
    return response

def test_get_student():
    response_creating = create_test_student()
    response_body = response_creating.json()
    student_id = response_body["info"][0]["id"]
    print(f"Создали студента с id={student_id}, пытаемся отправить get")

    response = requests.get(url=(URL_GET_STUDENT + str(student_id)))
    response_body = response.json()
    assert response.status_code == 200
    print("\nid студента:", response_body["info"][0]["id"])
    print("Время проведения теста: ", datetime.datetime.now())


def test_get_error_student():
    response = requests.get(url=(URL_GET_STUDENT + "2100000000000"))
    response_body = response.json()   
    assert response.status_code == 201
    print("Студента с таким id не существует!")
    print("Время проведения теста: ", datetime.datetime.now())


if __name__ == "__main__":
    pytest.main([__file__])