from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/' , user_Login , name='loginpage'),

    path('register/' , user_Register , name='registerpage'),

    path('logout/' , user_logout , name='logout'),

    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="reset_password/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="reset_password/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/password_reset_done.html"), 
        name="password_reset_complete"),


]