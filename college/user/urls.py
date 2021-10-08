from os import name
from django.urls import path
from .views import *



urlpatterns = [

    path('' , Home , name='homepage'),

    path('About us/' , About , name='aboutpage'),

    path('department/views/' , department_view , name='departments'),

    path('department/details/<id>/' , department_details , name='departments_details'),

    path('activity/views/' , Activity_view , name='activities'),

    path('activity/details/<id>/' , Activity_details , name='activity_details'),

    path('facility/view/' , Factility_view , name='facilities'),

    path('facility/details/<id>/' , Facility_details , name='Facility_details'),

    path('contact/' , ContactCreateView , name='contact'),

    path('student/' , student_home , name='student_home'),

    path('student/subjects/<int:id>/', student_subject , name='student_subject' ),

    path('student/notes/download/<int:id>/' , studentFile_download , name='student_file')


]