from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Student, Instructor, Admin


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # https: // docs.djangoproject.com / en / 4.0 / ref / forms / widgets /  #:~:text=A%20widget%20is%20Django's%20representation,DOCTYPE%20html%3E%20.
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # This is for the username and password fields which we cannot access directly
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['pattern'] = "[APS]{1}[A-Za-z0-9@\/.\/+\/-\/_ ]{0,}"
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class SCompleteRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            'name': 'Username'
        }


class PCompleteRegistrationForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = "__all__"


class ACompleteRegistrationForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
