import json

import pytest
import requests

#####   GET Method   ########

list_of_students_to_check = [1,2,3,4]

@pytest.mark.parametrize("student",list_of_students_to_check)
def test_check_student(student):
    data = {}
    url = "http://127.0.0.1:8000/student/%s" %student
    response = requests.get(url, data= data)
    assert response.status_code == 200

#####   POST METHOD    ##########

add_new_student = [["4",'prabhas', "4003"]]

list_of_new_students_to_be_added = [["6","Pavan","4005"],["7","Pavani","4006"]]

@pytest.mark.parametrize("id, name, roll_no",add_new_student)
def test_create_student(id,name,roll_no):
    url = "http://127.0.0.1:8000/student"
    json_data = {"id":id, "name":name, "roll_no": roll_no}
    response = requests.post(url, json = json_data)
    assert response.status_code == 201






    


