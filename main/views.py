from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, LoginForm
from .models import *
from django.http import HttpResponse
import csv
from .forms import *
from .mixins import MessaHandler
import random
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404

# Create your views here.

#STATION-USER INTERFACE

def registerPage(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        try:
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('index')
        except Exception as e:
            print(e)
            raise

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def loginPage(request):
    form = LoginForm()

    if request.method == 'POST':
        try:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('index')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')

def index(request):

    return render(request,'index.html')

@login_required
def Dashboard(request):
    
    user= request.user
    if request.user.is_authenticated:
        user_station = request.user.station
        categry = Category.objects.all()
        cat1 = FeedbackForm.objects.filter(station=user_station, category__categ='others').count()
        cat2 = FeedbackForm.objects.filter(station=user_station, category__categ='senior citizen').count()
        cat3 = FeedbackForm.objects.filter(station=user_station, category__categ='Behaviour').count()
        cat4 = FeedbackForm.objects.filter(station=user_station, category__categ='Cleanliness').count()
        total_feedbacks = FeedbackForm.objects.filter(station=user_station).count()
        user_station = request.user.station
        feedbacks = FeedbackForm.objects.filter(station=user_station)
        qr=Station.objects.filter(qr_code=user_station)
    #feedbacks = FeedbackForm.objects.filter(station_id=station_id)
    

    context ={
        'cat1':cat1,
        'cat2':cat2,
        'cat3':cat3,
        'cat4':cat4,
        'categry' :categry,
        'total_feedbacks' :  total_feedbacks,
        'user' : user,
       'feedbacks': feedbacks,
       'qr':qr,
    }

    return render(request, 'Dashboard.html',context)

def about(request):

    return render(request, 'about.html')

def export_to_csv(request):
    user= request.user
    if request.user.is_authenticated:
        user_station = request.user.station
        feedbacks = FeedbackForm.objects.filter(station=user_station)
        response= HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=feedbacks.csv'
        writer = csv.writer(response)
        writer.writerow(('Name','Email','City','Station','Category','Description'))
        feedback_fields=FeedbackForm.objects.filter(station=user_station).values_list('name','email','city','station','category','description')

        for feedback in feedback_fields:
            writer.writerow(feedback)
        return(response)
    
def get_qr(request):

    user= request.user
    # Open the QR code image file using the storage backend
    with default_storage.open(Station.qr_code.name, 'rb') as f:
        image_data = f.read()

    # Create the HTTP response with the image file as its content
    response = HttpResponse(image_data, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="{Station.qr_code.name}"'
    return response



def download_qr_code(request, station_id):
    # Retrieve the Station instance
    station = get_object_or_404(Station, station_Id=station_id)

    # Open the QR code image file using the storage backend
    with default_storage.open(station.qr_code.name, 'rb') as f:
        image_data = f.read()

    # Create the HTTP response with the image file as its content
    response = HttpResponse(image_data, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="{station.qr_code.name}"'
    return response

def qr(request):
    return render(request, 'qr.html')

def create_view(request):
    form = Feedback()
    if request.method == 'POST':
        form = Feedback(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    return render(request, 'form.html', {'form': form})

# AJAX
def load_stations(request):
    city_id = request.GET.get('city_id')
    stations = Station.objects.filter(city_id=city_id).all()
    return render(request, 'station_dropdown_list_options.html', {'stations': stations})

def thankyou(request):

    return render(request,'success.html')

def otp_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        #user =User.objects.create(username = username)
        profile = Profile(username = username, phone_number = phone_number)

        profile.otp = random.randint(1000, 9999)
        profile.save()
        message_handler = MessaHandler(phone_number , profile.otp).send_otp_on_phone()
        
        return redirect(f'/otp/{profile.uid}')
    return render(request, 'otp_s.html')

def otp_input(request, uid):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile= Profile.objects.get(uid=uid)
        if otp == profile.otp:
            #login(request,profile.username)
            return redirect('/feedback/add/')

        return redirect(f'/otp/{uid}')

    return render(request, 'otp.html')

def thankyou(request):

    return render(request,'success.html')