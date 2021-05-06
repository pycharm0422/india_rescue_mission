from django.urls import path
from . import views
urlpatterns = [
    path('patient_form/', views.telemedicineForm, name='patient-page'),
    # path('doctor_form/', views.doctorForm, name='doctor-form'),
    path('patient_or_doctor/', views.patient_or_doctor, name='doc_or_pt'),
    path('charge/', views.charge, name='charge'),
    path('messages/', views.mssgs, name='messages-page'),
    path('messagesboard/', views.messagesboard, name='message-board-form'),
    path('dashboard/', views.dashboard, name='dashboard-page'),
    path('volunteer-form/', views.volunteer, name='volunteer-page'),
    path('doctor-form/', views.doctor, name='doctor-page'),
    path('donor-form/', views.donor, name='donor-page'),
    path('councellor-form/', views.councellor, name='counsellor-page'),
    path('success/<str:args>', views.successMsg, name='success'),
    path('', views.home3, name='home-page'),
    path('index/', views.index, name='index-page'),
    path('health_care_providers/', views.health_care, name='health_care_prov'),
    path('safety_measure/', views.safety_measure, name='safety-measure'),
]