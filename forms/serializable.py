from django.conf.urls import url, include
from django.contrib.auth.models import User
from onlineapp.models import*
from rest_framework import routers, serializers, viewsets


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        # exclude = ['id']
        fields = ['name', 'location', 'acronym']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # exclude = ['college_id', 'dob', 'id']
        fields = ['name', 'dropped_out', 'db_folder', 'email']


class MockTestSerializable(serializers.ModelSerializer):
    class Meta:
        model=MockTest1
        fields = ['problem1', 'problem2', 'problem3', 'problem4', 'total']