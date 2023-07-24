import json

import pytest
import requests

#####  CHECKING STUDENTS USING GET Method   ########

list_of_students_to_check = [1,2,3,4]

@pytest.mark.parametrize("student",list_of_students_to_check)
def test_check_student(student):
    data = {}
    url = "http://127.0.0.1:8000/student/%s" %student
    response = requests.get(url, data= data)
    assert response.status_code == 200

#####   ADDING STUDENTS USING POST METHOD    ##########

add_new_student = [["4",'prabhas', "4003"]]

list_of_new_students_to_be_added = [["6","Pavan","4005"],["7","Pavani","4006"]]

@pytest.mark.parametrize("id, name, roll_no",add_new_student)
def test_create_student(id,name,roll_no):
    url = "http://127.0.0.1:8000/student"
    json_data = {"id":id, "name":name, "roll_no": roll_no}
    response = requests.post(url, json = json_data)
    assert response.status_code == 201


## MISSING PARAMETERS or wrong parameters -- 400 Bad Request

missing_parameters = [["4", "some_name", "name"], ["suresh", "ramesh", "345"], ["3","6", "dummy_name"]]

@pytest.mark.parametrize("id,name, roll_no", missing_parameters)
def test_check_wrong_parameters(id, name, roll_no):
    url = "http://127.0.0.1:8000/student"
    json_data = {"id":id, "name":name, "roll_no": roll_no}
    response = requests.post(url, json = json_data)
    assert response.status_code == 400

missing_parameters = [["4"], ["suresh"], ["3"]]

missing_parameters = [["4", "some_name"], ["suresh", "ramesh"], ["3","6"]]

@pytest.mark.parametrize("id,name", missing_parameters)
def test_check_student(id, name, roll_no=None):
    url = "http://127.0.0.1:8000/student"
    json_data = {"id":id, "name":name, "roll_no": roll_no}
    response = requests.post(url, json = json_data)
    assert response.status_code == 400

missing_parameters = [["4"], ["suresh"], ["3"]]

@pytest.mark.parametrize("id", missing_parameters)
def test_check_parameters(id, name=None, roll_no=None):
    url = "http://127.0.0.1:8000/student"
    json_data = {"id":id, "name":name, "roll_no": roll_no}
    response = requests.post(url, json = json_data)
    assert response.status_code == 400








    


