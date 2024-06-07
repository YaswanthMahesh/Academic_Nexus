from django.views import View
from django.urls import resolve
from django.shortcuts import render, redirect
from onlineapp.forms import loginForms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


class signupForm_view(View):
    def get(self, request, *args, **kwargs):
        signupform = loginForms.SignupForm()
        return render(
            request,
            template_name='signupform.html',
            context={
                'form': signupform
            }
        )

    def post(self,request):
        form = loginForms.SignupForm(request.POST)
        if form.is_valid():
            try:
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                username = request.POST['username']
                password = request.POST['password']
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password)
                user.save()
            except:
                messages.error(request, 'Invalid Credentials')
                return redirect('signup')

            return redirect('login')

        else:
            return redirect('signup')
