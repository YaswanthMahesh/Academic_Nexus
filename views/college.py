from django.views import View
from django.urls import resolve
from onlineapp.models import *
from django.shortcuts import render, redirect
from onlineapp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


def logout_user(request):
    logout(request)
    return redirect("login")


class class_view(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        if kwargs:
            college = College.objects.values('name', 'acronym', 'id').filter(acronym=kwargs['acronym'])
            students = Student.objects.values('name', 'college__name', 'mocktest1__total', 'id').filter(college__acronym=kwargs['acronym'])
            return render(
                request,
                template_name='index2.html',
                context={
                    'values': students,
                    'title': 'Students from {}'.format(college[0]['name']),
                    'id': kwargs['pk']
                }
            )
        college = College.objects.values('name', 'acronym', 'id')
        return render(
            request,
            template_name="index.html",
            context={
                "values": college,
            }
        )


class AddCollegeView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, **kwargs):
        form = CollegeForm()

        if kwargs:
            college = College.objects.get(id=kwargs['pk'])
            form = CollegeForm(instance=college)

        return render(
            request,
            template_name="AddForm.html",
            context={
                "form": form
            }
        )

    def post(self, request, **kwargs):

        if resolve(request.path_info).url_name == 'deletecollege':
            College.objects.get(id=kwargs['pk']).delete()
            return redirect('colleges')

        if resolve(request.path_info).url_name == 'editcollege':
            college = College.objects.get(id=kwargs.get('pk'))
            form = colleges.CollegeForm(request.POST, instance=college)
        if kwargs:
            if form.is_valid():
                form.save()
                return redirect('colleges')

        form = colleges.CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colleges')


class AddStudentView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, **kwargs):
        form1 = StudentForm
        form2 = MockTestForm
        if resolve(request.path_info).url_name == 'deletestudent':
            Student.objects.get(id=kwargs['id']).delete()
            return redirect('colleges')

        if resolve(request.path_info).url_name == 'editstudent':
            student = Student.objects.get(id=kwargs['id'])
            form1 = StudentForm(instance=student)
            s1 = MockTest1.objects.get(student_id=kwargs['id'])
            form2 = MockTestForm(instance=s1)

        if kwargs and not(resolve(request.path_info).url_name == 'editstudent'):
            college = College.objects.get(id=kwargs['pk'])
            s = Student(college=college)
            form1 = StudentForm(instance=s)
            s1 = MockTest1(student=s)
            form2 = MockTestForm(instance=s1)

        return render(
            request,
            template_name="AddStudent.html",
            context={
                "form1": form1,
                "form2": form2
            }
         )

    def post(self, request, **kwargs):
        if resolve(request.path_info).url_name == 'editstudent':
            student = Student.objects.get(id=kwargs['id'])
            mocktest = MockTest1.objects.get(student_id=kwargs['id'])
            form1 = colleges.StudentForm(request.POST, instance=student)
            form2 = colleges.MockTestForm(request.POST, instance=mocktest)
            form1.save()
            form2.save()
            return redirect('colleges')

        college = College.objects.get(**kwargs)
        s = Student(college=college)
        form1 = colleges.StudentForm(request.POST, instance=s)
        form1.save()
        s1 = MockTest1(student=s)
        form2 = colleges.MockTestForm(request.POST, instance=s1)
        form2.save()
        return redirect('colleges')

