from django.urls import path
from .views import *



urlpatterns = [

    path('dashbord/',admin_dashboard , name='adminhome'),

    path('Department/create/' , DepartmentCreateView.as_view() , name='add_department'),

    path('Department/list/' , DepartmentListView.as_view() , name='department_list'),

    path('Department/update/<id>/' , DepartmentUpdateView.as_view() , name='department_update'),

    path('department/delete/<id>/', Remove_department , name='Remove_department'),

    path('Activity/create/' , ActivityCreateView.as_view() , name='activity_create'),

    path('Activity/List/' , Activity_list , name='activity_list'),

    path('Activity/update/<id>/' , ActivityUpdateView.as_view() , name='activity_update'),

    path('acttivity/delete/<id>' , remove_activity , name='activity_delete'),

    path('Facility/create/',FacilityCreateView.as_view() , name='facility_create'),

    path('facility/list/' , Facility_list , name='facility_list'),

    path('facility/update/<id>/' , FacilityUpdateView.as_view() , name='facility_update'),
    
    path('facility/delete/<id>/' , remove_facility_list , name='delete_facility_list'),
    
    path('teachers/create/' , TeacherCreateView.as_view() , name='add_teachers'),

    path('teachers/list/' , teacher_list , name='teachers_list'),

    path('teachers/update/<id>/' , TeachersUpdateView.as_view() , name='teachers_update'),

    path('teachers/delete/<id>/' , remove_teacher_list , name='remove_teacher_list'),

    path('student/registration/' , student_register , name='student_create'),

    path('student/add/' , student_add , name='student_add') , 

    path('student/remove/<int:id>/' , remove_student_list , name='remove_student'),

    path('staff/create/' , staff_user_register , name='staff_register'),

    path('staff/list/' , staff_list , name='staff_list'),

    path('staff/remove/<int:id>/' , remove_staff_list , name='remove_staff'),

    path('announcements/create/' , AnnouncementsCreateView.as_view() , name='announcements_create'),

    path('announcements/list/' , announcement_list , name='announcement_list'),

    path('announcements/update/<int:id>/' , AnnouncementsUpdateView.as_view() , name='announcements_update'),

    path('announcements/delete/<int:id>' , remove_announcements_list , name='remove_announcements_list')



]