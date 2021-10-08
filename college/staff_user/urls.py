from django.urls import path
from .views import *




urlpatterns = [
    
    path('home/' , staff_home , name='staff_home'),

    path('subject/create/' , SubjectCreateView.as_view() , name='subject_create_view'),

    path('subject/list/' , SubjectListView.as_view() , name='subject_list_view' ),

    path('subject/update/<int:id>/' , SubjectUpdateView.as_view() , name='subject_update_view'),

    path('subject/delete/<id>' , subject_delete , name='subject_delete_view'),

    path('notes/create/' , NotesCreateView.as_view() , name='notes_create_view'),

    path('notes/list/' , NotesListView.as_view() , name='notes_list'),

    path('notes/update/<int:id>/' , NotesUpdateView.as_view() , name='notes_update'),

    path('notes/delete/<int:id>/' , notes_delete , name='notes_delete')

]