import json

import pytest
import requests

list_of_students_to_check = [1,2,3]

@pytest.mark.parametrize("student",list_of_students_to_check)
def test_check_student(student):
    data = {}
    url = "http://127.0.0.1:8000/student/%s" %student
    response = requests.get(url, data= data)
    assert response.status_code == 200






    


