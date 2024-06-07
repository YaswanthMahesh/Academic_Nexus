from django.views import View
from django.urls import resolve
from django.shortcuts import render, redirect
from onlineapp.forms import loginForms
from django.contrib.auth import authenticate, login
from django.contrib import messages


class loginForm_view(View):
    def get(self, request, *args, **kwargs):
        loginform = loginForms.LoginForm()
        return render(
            request,
            template_name='loginform.html',
            context={
                'form': loginform
            }
        )

    def post(self, request):
        form = loginForms.LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('colleges')
            else:
                # messages.add_messages(request, messages.INFO, 'Invalid Credentials')
                messages.error(request,'Invalid Credentials')
                return redirect('login')
        # return redirect('colleges')