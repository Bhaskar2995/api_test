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
        name = data.get('name')
        roll_no = data.get('roll_no')
       
        if not id or not name or not roll_no:
            message = "Missing Details"
            return JsonResponse(data = {'response':message},status = 400)
        
        if type(id) != int:
            message = "id should be an integer"
            return JsonResponse(data = {'response':message},status = 400)
        
        if type(name) != str:
            message = "name should be string"
            return JsonResponse(data = {'response':message},status = 400)
        
        if type(roll_no) != int:
            message = "id should be an integer"
            return JsonResponse(data = {'response':message},status = 400)
        
        
        try:
            student = Student.objects.get(id = id)
            print(student.name)
            message = "A student already exists for this id. The student's name is: %s" %student.name
            return JsonResponse(data = {'response': message})
        except:
            student = Student(id = id, name = name, roll_no = roll_no)
            student.save()
            return JsonResponse(data = {'response': "Successfully added new student"},status = 201)


