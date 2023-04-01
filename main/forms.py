from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'required': True,
                'placeholder': '20CS060@charusat.edu.in',
                'autofocus': True
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
            })
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'placeholder': 'Password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'Confirm Password'}

class LoginForm(AuthenticationForm):
    class Meta:
        fields = '__all__'



class Feedback(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = '__all__'
        #'video' : forms.FileField(allow_empty_file=True)
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'city': forms.Select(attrs={ 'class': 'form-select' }),
            'station': forms.Select(attrs={ 'class': 'form-select' }),
            'category': forms.Select(attrs={ 'class': 'form-select' }), 
            'description': forms.Textarea( {'class': 'form-control'}), 
            #'image':forms.ImageField(allow_empty_file=True,),
        }    
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['station'].queryset = Station.objects.none()
 
        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['station'].queryset = Station.objects.filter(city_id=city_id).order_by('station_Id')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['station'].queryset = self.instance.city.station_set.order_by('station_Id')

