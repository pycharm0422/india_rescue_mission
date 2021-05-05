from django.shortcuts import render, redirect
from .forms import DoctorsForms, TeleMedicineForms, MessagesForm
from django.contrib import messages
from django.urls import reverse
import stripe
from django.http import JsonResponse
from .models import Resource, City, Messages

stripe.api_key = "sk_test_51IkYavSEV2gnCPG20RfHko44Y1eooN01Kjd9bMU9vGo5a2WlNNr5XYqKoLKWBlLvkY3TGDv2evZMHO24EnMNrLUT00n1k2ztHs"
def home(request):
    return render(request, 'rescue/home.html')

def home2(request):
    return render(request, 'rescue/home2.html')

def patient_or_doctor(request):
    if request.method == 'POST':
        # for key, value in (request.POST).items:
        ch_len = len(list(request.POST))
        choice = list(request.POST)[-1]
        if choice == 'patient' and ch_len <=2:
            return redirect('patient-form')
        elif choice == 'doctor' and ch_len <=2:
            return redirect('doctor-form')
        else:
            return redirect('doc_or_pt')
    return render(request, 'rescue/patient_or_doctor.html')

def telemedicineForm(request):
    if request.method == 'POST':
        form = TeleMedicineForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Patient form submitted {username}')

        return redirect('home-page')
    else:
        form = TeleMedicineForms()
    context = {
        'form':form,
    }
    return render(request, 'rescue/patient_form.html', context)

def doctorForm(request):
    if request.method == 'POST':
        form = DoctorsForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Doctor form submitted {username}')
        return redirect('home-page')
    else:
        form = DoctorsForms()

    context = {
        'form':form,
    }
    return render(request, 'rescue/doctor_form.html', context)


def health_care(request):
    return render(request, 'rescue/health_care_prov.html')



def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))
def successMsg(request, args):
    amount = args
    return render(request, 'rescue/success.html', {'amount':amount})

def safety_measure(request):
    return render(request, 'rescue/safety.html')

def home3(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['Name']
        contact = request.POST['Contact']
        city = request.POST['City']
        state = request.POST['State']
        country = request.POST['Country']
        message = request.POST['Message']
        form = Messages.objects.create(name=name, contact=contact, city=city, state=state, country=country, message=message)
       

    resources = Resource.objects.all()
    messages = Messages.objects.order_by('-pk')[0:3]
    context = {
        'resources':resources,
        'messages':messages,
    }
    return render(request, 'rescue/home3.html', context)


def index(request):
    return render(request, 'rescue/index.html')

def mssgs(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['Name']
        contact = request.POST['Contact']
        city = request.POST['City']
        state = request.POST['State']
        country = request.POST['Country']
        message = request.POST['Message']
        form = Messages.objects.create(name=name, contact=contact, city=city, state=state, country=country, message=message)
    mssges = Messages.objects.order_by('-pk')
    context = {
        'mssges':mssges,
    }
    return render(request, 'rescue/messages.html', context)