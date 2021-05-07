from django.forms import ModelForm
from .models import Telemedicine, Doctor, Messages,MessageBoard, Donor, Counsellor, Volunteer, OxygenShortageHospital
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

gndr = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others', 'Others'),
)

class DoctorsForms(UserCreationForm):
    name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=gndr)
    specilization = forms.CharField()
    years_of_practice = forms.IntegerField()
    hospital_name = forms.CharField()
    consulting_hour = forms.CharField()
    address = forms.CharField(max_length=200, widget=forms.TextInput({}))
    contact = forms.IntegerField()
    email = forms.EmailField()
    profile = forms.CharField(max_length=200, min_length=5)
    city = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'name', 'age', 'gender', 'specilization', 'years_of_practice', 'hospital_name', 'consulting_hour', 'address', 'contact', 'email', 'profile', 'city', 'state', 'country', 'password1', 'password2']

class TeleMedicineForms(UserCreationForm):
    name = forms.CharField(label='Enter your name',widget=forms.TextInput(attrs={'placeholder': ''}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=gndr, initial='None')
    address = forms.CharField(max_length=200)
    oxygen_saturation = forms.CharField()
    pulse = forms.CharField()
    person_accompany_name = forms.CharField(max_length=200, min_length=2, required=False)
    person_accompany_phone = forms.CharField(max_length=200, min_length=2, required=False)
    contact = forms.IntegerField()
    email = forms.EmailField()
    profile = forms.CharField(max_length=200, min_length=5)
    city = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'name', 'age', 'gender', 'address', 'oxygen_saturation', 'pulse', 'person_accompany_name', 'person_accompany_phone', 'contact', 'email', 'profile', 'city', 'state', 'country', 'password1', 'password2']

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'

class MessageBoardForm(ModelForm):
    class Meta:
        model = MessageBoard
        fields = '__all__'

class VolunteerForm(UserCreationForm):
    name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=gndr)
    address = forms.CharField(max_length=200, widget=forms.TextInput({}))
    contact = forms.IntegerField()
    email = forms.EmailField()
    profile = forms.CharField(max_length=200, min_length=5)
    city = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'name', 'age', 'gender', 'address', 'contact', 'email', 'profile', 'city', 'state', 'country', 'password1', 'password2']


class DonorForm(UserCreationForm):
    name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=gndr)
    blood_group = forms.CharField()
    address = forms.CharField(max_length=200, widget=forms.TextInput({}))
    contact = forms.IntegerField()
    email = forms.EmailField()
    profile = forms.CharField(max_length=200, min_length=5)
    city = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'name', 'age', 'gender', 'blood_group', 'address', 'contact', 'email', 'profile', 'city', 'state', 'country', 'password1', 'password2']

class CounsellerForm(UserCreationForm):
    name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=gndr)
    address = forms.CharField(max_length=200, widget=forms.TextInput({}))
    contact = forms.IntegerField()
    email = forms.EmailField()
    profile = forms.CharField(max_length=200, min_length=5)
    city = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'name', 'age', 'gender','address', 'contact', 'email', 'profile', 'city', 'state', 'country', 'password1', 'password2']

class OxygenShortageHospitalForm(ModelForm):
    class Meta:
        model =OxygenShortageHospital
        fields = "__all__"