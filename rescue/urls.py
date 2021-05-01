from django.urls import path
from . import views
urlpatterns = [
    path('patient_form/', views.telemedicineForm, name='patient-form'),
    path('doctor_form/', views.doctorForm, name='doctor-form'),
    path('patient_or_doctor/', views.patient_or_doctor, name='doc_or_pt'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>', views.successMsg, name='success'),
    path('', views.home3, name='home-page'),
    path('index/', views.index, name='index-page'),
    path('health_care_providers/', views.health_care, name='health_care_prov'),
    path('safety_measure/', views.safety_measure, name='safety-measure'),
]