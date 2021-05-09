from django.shortcuts import render, redirect
from .forms import DoctorsForms, TeleMedicineForms, MessagesForm, MessageBoardForm, VolunteerForm, DonorForm, CounsellerForm, OxygenShortageHospitalForm
from django.contrib import messages
from django.urls import reverse
import stripe
from django.http import JsonResponse
from .models import Resource, City, Messages, MessageBoard, Volunteer, Donor, Doctor, Telemedicine, Counsellor, OxygenShortageHospital
from django.contrib.auth import login, authenticate


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

        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        oxygen_saturation = request.POST['oxygen_saturation']
        pulse = request.POST['pulse']
        person_accompany_name = request.POST['person_accompany_name']
        person_accompany_phone = request.POST['person_accompany_phone']
        contact = request.POST['contact']
        email = request.POST['email']
        profile = request.POST['profile']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        form = TeleMedicineForms(request.POST)
        if form.is_valid():
            print("working ....")
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
        
        Telemedicine.objects.create(username=request.user, name=name, age=age, gender=gender, address=address, oxygen_saturation=oxygen_saturation, pulse=pulse, person_accompany_name=person_accompany_name, person_accompany_phone=person_accompany_phone, contact=contact, email=email, profile=profile, city=city, state=state, country=country)
        return redirect('home-page')
    else:
        form = TeleMedicineForms()

    context = {
        'form':form,
    }

    return render(request, 'rescue/patient.html', context)

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
    form2 = MessageBoardForm()
    bdmsgs = MessageBoard.objects.order_by('-pk')[0:3]
    resources = Resource.objects.all()
    messages = Messages.objects.order_by('-pk')[0:3]
    form3 = OxygenShortageHospitalForm()
    shortage_beds = OxygenShortageHospital.objects.order_by('-pk')[0:3]
    context = {
        'resources':resources,
        'messages':messages,
        'form2':form2,
        'bdmsgs':bdmsgs,
        'form3':form3,
        'shortage_beds':shortage_beds,
        
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


def dashboard(request):
    return render(request, 'rescue/dashboard.html')

def messagesboard(request):
    if request.method == 'POST':
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home-page')


def volunteer(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        profile = request.POST['profile']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        form = VolunteerForm(request.POST)
        if form.is_valid():
            print("working ....")
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
        
        Volunteer.objects.create(user=request.user, name=name, age=age, gender=gender, address=address, contact=contact, email=email, profile=profile, city=city, state=state, country=country)
        return redirect('home-page')
    else:
        form = VolunteerForm()

    context = {
        'form':form,
    }

    return render(request, 'rescue/volunteers.html', context)

def donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        profile = request.POST['profile']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
        Donor.objects.create(user=request.user, name=name, age=age, gender=gender, blood_group=blood_group, address=address, contact=contact, email=email, profile=profile, city=city, state=state, country=country)
        return redirect('home-page')
    else:
        form = DonorForm()
    context = {
        'form':form
    }
    return render(request, 'rescue/donor.html', context)

def doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        specilization = request.POST['specilization']
        years_of_practice = request.POST['years_of_practice']
        hospital_name = request.POST['hospital_name']
        consulting_hour = request.POST['consulting_hour']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        profile = request.POST['profile']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        form = DoctorsForms(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
        Doctor.objects.create(username=request.user,name=name, age=age, gender=gender, specilization=specilization, years_of_practice=years_of_practice, hospital_name=hospital_name, consulting_hour=consulting_hour, address=address, contact=contact, email=email, profile=profile, city=city, state=state, country=country)
        return redirect('home-page')
    else:
        form = DoctorsForms()
    context = {
        'form':form
    }
    return render(request, 'rescue/doctor.html', context)

def councellor(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        profile = request.POST['profile']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        form = CounsellerForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
        Counsellor.objects.create(user=request.user, name=name, age=age, gender=gender, address=address, contact=contact, email=email, profile=profile, city=city, state=state, country=country)
        return redirect('home-page')
    else:
        form = CounsellerForm()
    context = {
        'form':form
    }
    return render(request, 'rescue/councellor.html', context)

def board(request):
    if request.method == 'POST':
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home-page')
    bdmsgs = MessageBoard.objects.order_by('-pk')
    form = MessageBoardForm()
    context = {
        'mssges':bdmsgs,
        'form':form,
    }

    return render(request, 'rescue/board.html', context)


def oxygen_shortage(request):
    if request.method == 'POST':
        form = OxygenShortageHospitalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('oxygen-shortage-page')

    form = OxygenShortageHospitalForm()
    shortages = OxygenShortageHospital.objects.order_by('-pk')

    context = {
        'form':form,
        'mssges':shortages,
    }
    return render(request, 'rescue/oxygen_shortages.html', context)

def donatenow(request):
    return render(request, 'rescue/donatenow.html')

    