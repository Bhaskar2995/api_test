import json

from django.http import JsonResponse
from django.views import View


class Student(View):
    def get(self,request,*args, **kwargs):
        id = kwargs['id']
        student = Student.objects.get(id = id)
        data = {'name': student.name, 'roll_no': student.roll_no}
        return JsonResponse(data)
    def post(self,request,*args, **kwargs):
        data = json.loads(request.body)
        id = data.get('id')
        name = data.get('name')
        roll_no = data.get('roll_no')
        student = Student(id = id, name = name, roll_no = roll_no)
        student.save()

