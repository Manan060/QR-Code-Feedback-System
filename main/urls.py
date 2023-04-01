from django.urls import path
from . import views

urlpatterns = [

    #StationUser
    path('register/', views.registerPage, name='register'),
    path('', views.loginPage, name='login'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('about/',views.about,name='about'),
    path('export-to-csv',views.export_to_csv,name='export-to-csv'),
    path('qr_code/',views.get_qr,name='get_qr'),
    path('qr/',views.qr,name='qr'),
    path('stations/<int:station_id>/qr_code/', views.download_qr_code, name='download_qr_code'),

    #Citizen
    
    path('otp/<uid>/',views.otp_input,name='otp'),
    path('otpView/',views.otp_view,name='otpV'),
    path('member/ajax/load-stations/', views.load_stations, name='ajax_load_stations'), # AJAX
    path('feedback/add/', views.create_view, name='add'),
    path('thankyou/',views.thankyou,name="thankyou"),

]