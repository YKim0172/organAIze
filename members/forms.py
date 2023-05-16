from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, SearchRequest
from django import forms
from django.forms import ModelForm

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2',)
    
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'form-control w-50',
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'form-control w-50',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control w-50',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype your password',
        'class': 'form-control w-50',
    }))


class EditCoursesTakenForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('taken_EECS110', 'taken_EECS183',
                  'taken_EECS200', 'taken_EECS201', 'taken_EECS203', 'taken_EECS215', 'taken_EECS216', 'taken_EECS230', 'taken_EECS270', 'taken_EECS280', 'taken_EECS281', 'taken_EECS298',
                  'taken_EECS300', 'taken_EECS301', 'taken_EECS311', 'taken_EECS312', 'taken_EECS314', 'taken_EECS320', 'taken_EECS330', 'taken_EECS334', 'taken_EECS351', 'taken_EECS370', 'taken_EECS373', 'taken_EECS376', 'taken_EECS388', 'taken_EECS399',
                  'taken_EECS402', 'taken_EECS409', 'taken_EECS411', 'taken_EECS413', 'taken_EECS414', 'taken_EECS421', 'taken_EECS423', 'taken_EECS427', 'taken_EECS428', 'taken_EECS434', 'taken_EECS435', 'taken_EECS441', 'taken_EECS442', 'taken_EECS443',
                  'taken_EECS445', 'taken_EECS452', 'taken_EECS453', 'taken_EECS455', 'taken_EECS458', 'taken_EECS460', 'taken_EECS461', 'taken_EECS463', 'taken_EECS464', 'taken_EECS465', 'taken_EECS467', 'taken_EECS470', 'taken_EECS471', 'taken_EECS473',
                  'taken_EECS475', 'taken_EECS477', 'taken_EECS482', 'taken_EECS483', 'taken_EECS484', 'taken_EECS485', 'taken_EECS487', 'taken_EECS489', 'taken_EECS490', 'taken_EECS491', 'taken_EECS492', 'taken_EECS494', 'taken_EECS495', 'taken_EECS496', 'taken_EECS497', 'taken_EECS498', 'taken_EECS499',
                  'taken_EECS501', 'taken_EECS507', 'taken_EECS517', 'taken_EECS520', 'taken_EECS523', 'taken_EECS530', 'taken_EECS540', 'taken_EECS542', 'taken_EECS544', 'taken_EECS551', 'taken_EECS553', 'taken_EECS554', 'taken_EECS558', 'taken_EECS560',
                  'taken_EECS561', 'taken_EECS563', 'taken_EECS564', 'taken_EECS574', 'taken_EECS575', 'taken_EECS582', 'taken_EECS584', 'taken_EECS587', 'taken_EECS595', 'taken_EECS598', 'taken_EECS599', 'taken_EECS628')

class UserSearchForm(forms.ModelForm):
    class Meta:
        model = SearchRequest
        fields = ('user_request',)
        widgets = {
            'user_request': forms.TextInput(attrs={
                                        'class': 'form-control text-white col-lg-5',
                                        'style': 'font-family: Cambria; background-color: rgb(22, 22, 22); border-color: white; border-width: 5px; margin-left: auto; margin-right: auto; background-color: white; margin-top: 500px;',
                                        'rows': '6',
            })
        }