from django.forms import Form, CharField, EmailField, TextInput, PasswordInput, EmailInput


class SignUpForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control',
    }))
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control',
    }))


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
    }))
