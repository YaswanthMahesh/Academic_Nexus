from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from onlineapp.forms.serializable import CollegeSerializer
from onlineapp.models import *


@api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
def r_collegeview(request):
    if request.method == 'GET':
        c = College.objects.all()
        collegeSerializableData = CollegeSerializer(c, many=True)
        return Response(collegeSerializableData.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
