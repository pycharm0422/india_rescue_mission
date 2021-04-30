from django.forms import ModelForm
from .models import Telemedicine, Doctor


class DoctorsForms(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ('username',)

class TeleMedicineForms(ModelForm):
    class Meta:
        model = Telemedicine
        fields = '__all__'
        exclude = ('username',)