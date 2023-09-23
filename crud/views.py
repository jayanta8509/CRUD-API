from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    employ_obj = student.objects.all()
    serializer = studentSerializer(employ_obj , many=True)
    return Response({'status' : 200 ,  'payload' : serializer.data})

@api_view(["POST"])
def post_student(request):
    data = request.data
    # print(data)
    serializer = studentSerializer(data=request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'ststus': 403 , 'errors' : serializer.errors, 'messge':'Something went wrong'})
    serializer.save()
    return Response({'status':200, 'payload' : serializer.data,'messge':'your Data Saved'})

@api_view(['PUT'])
def update_student(request , id):
    try:
        student_obj = student.objects.get(id = id)
        serializer = studentSerializer(student_obj, data = request.data, partial= True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response ({'status':403, 'errors': 'serializer.errors','message':'not valid'})
        serializer.save()
        return Response({'status' :200 , 'payload': serializer.data, 'message':'your data has edit'})
    except Exception as e:
        print(e)
        return Response({'status':403, 'message':'invalid id'})

@api_view(['DELETE'])
# def delete_student (request ):
#     try:
#         id = request.GET.get('id')
#         # student_obj = student.objects.get(id = id)
#         student_obj.delete()
#         return Response({'status' : 200, 'message':'deleted'})
#     except Exception as e:
#         print(e)
#         return Response({'status':403,'message':'invalid id'})

def delete_student(request):          #http://127.0.0.1:8000/students/delete/?id=4 (for deleted using)
    try:
        id = request.GET.get('id')
        student_obj = student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200, 'message': 'deleted'})
    except student.DoesNotExist:
        return Response({'status': 404, 'message': 'Student with the provided id does not exist'})
    except Exception as e:
        print(e)
        return Response({'status': 500, 'message': 'Internal server error'})