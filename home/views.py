import json

from django.http import JsonResponse
from django.views import View

from .models import Student


class StudentView(View):
    def get(self,request,*args, **kwargs):
        id = kwargs['id']
        try:
            student = Student.objects.get(id = id)
        except:
            return JsonResponse(data = {}, status = 404)
        data = {'name': student.name, 'roll_no': student.roll_no}
        return JsonResponse(data)

    def post(self,request,*args, **kwargs):
        data = json.loads(request.body)
        id = data.get('id')
        print(id)
        name = data.get('name')
        print(name)
        roll_no = data.get('roll_no')
        student = Student(id = id, name = name, roll_no = roll_no)
        student.save()
        return JsonResponse(data = {'response': "Successfully added new student"},status = 201)

