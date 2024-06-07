from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from onlineapp.forms.serializable import StudentSerializer, MockTestSerializable
from onlineapp.models import *


@api_view(['GET', 'POST', 'DELETE'])
def r_studentview(request, **kwargs):
    if request.method == 'GET':
        s = Student.objects.filter(college__id=kwargs['pk'])
        studentSerializableData = StudentSerializer(s, many=True)
        return Response(studentSerializableData.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        college = College.objects.get(id=kwargs['pk'])
        student = Student(college=college)
        serializer = StudentSerializer(student, data=request.data)
        # serializer.college_id = kwargs['pk']
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student = Student.objects.get(id=request.data['id'])
        student.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def r_studentmocktestview(request, **kwargs):
    if request.method == 'POST':
        college = College.objects.get(id=kwargs['pk'])
        student = Student(college=college)
        studentserializer = StudentSerializer(student, data=request.data)
        if studentserializer.is_valid():
            studentserializer.save()
            mock = MockTest1(student=student)
            mocktestserializer = MockTestSerializable(mock, data=request.data['mocktest1'])
            if mocktestserializer.is_valid():
                mocktestserializer.save()
                return Response(studentserializer.data, status=status.HTTP_201_CREATED)
            return Response(mocktestserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(studentserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'DELETE':
