from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'enter password'})
    )


class SignupForm(forms.Form):
    firstname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter firstname'})
    )
    lastname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter lastname'})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'enter password'})
    )
