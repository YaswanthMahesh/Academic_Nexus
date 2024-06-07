from django import forms
from onlineapp.models import *


class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id']
        fields = ['name', 'location', 'acronym']

        # widgets = {
        # 'name': forms.CharField(attrs={'class': 'input', 'placeholder': 'enter your name'}),
        # 'location': forms.CharField(attrs={'class': 'input', 'placeholder': 'enter your location'}),
        # 'acronym': forms.CharField(attrs={'class': 'input', 'placeholder': 'enter college acronym'}),
        # 'contact': forms.EmailField(attrs={'class': 'input', 'placeholder': 'enter contact id'}),
        # }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['college_id', 'dob', 'id']
        fields = ['name', 'dropped_out', 'db_folder', 'email']


class MockTestForm(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['student_id', 'id']
        fields = ['problem1', 'problem2', 'problem3', 'problem4', 'total']
