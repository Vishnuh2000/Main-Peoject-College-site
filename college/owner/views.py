from django.contrib.auth.signals import user_logged_out
from django.shortcuts import get_object_or_404, render , redirect
from .models import *
from .forms import *
from django.views.generic import CreateView , UpdateView , ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from owner.models import *
from accounts.models import *
from accounts.forms import *



@login_required
def admin_dashboard(request):
    return render(request , 'admin_section/home.html')



class DepartmentCreateView(CreateView , LoginRequiredMixin):
    model = Department
    template_name = "department/add.html"
    form_class = DepartmentForm
    success_url = reverse_lazy('department_list')
    context_object_name = 'form'




class DepartmentListView(ListView , LoginRequiredMixin):
    model = Department
    template_name = "department/list.html"



class DepartmentUpdateView(UpdateView , LoginRequiredMixin):
    model = Department
    template_name = "department/add.html"
    form_class = DepartmentForm
    success_url = reverse_lazy('department_list')
    pk_url_kwarg = 'id'


@login_required
def Remove_department(request , id):
    remove_list = get_object_or_404(Department , pk=id)
    remove_list.delete()
    return redirect('department_list')
    


class ActivityCreateView(CreateView,LoginRequiredMixin):
    model = Activity
    template_name = "Activity/add.html"
    form_class = ActivityForm
    context_object_name = 'form'
    success_url = reverse_lazy('activity_list')



class ActivityUpdateView(UpdateView,LoginRequiredMixin):
    model = Activity
    template_name = "Activity/add.html"
    form_class = ActivityForm
    success_url = reverse_lazy('activity_list')
    pk_url_kwarg = 'id'


@login_required
def Activity_list(request):
    context={}
    context['activity'] = Activity.objects.all()
    return render(request , 'Activity/list.html' , context)

@login_required
def remove_activity(request,id):
    remove_list = get_object_or_404(Activity , id=id)
    remove_list.delete()
    return redirect('activity_list')


class FacilityCreateView(CreateView,LoginRequiredMixin):
    model = Facilities
    template_name = "facilities/add.html"
    form_class = FacilityForm
    success_url =reverse_lazy('facility_list')
    context_object_name ='form'



class FacilityUpdateView(LoginRequiredMixin,UpdateView):
    model = Facilities
    template_name = "facilities/add.html"
    form_class = FacilityForm
    success_url =reverse_lazy('facility_list')
    pk_url_kwarg = 'id'



@login_required
def Facility_list(request):
    context={}
    context['F_list'] = Facilities.objects.all()
    context['count'] = Facilities.objects.all().count()
    return render(request , 'facilities/list.html' , context)



@login_required
def remove_facility_list(request , id):
    remove_list = get_object_or_404(Facilities , id=id)
    remove_list.delete()
    return redirect('facility_list')




class TeacherCreateView(LoginRequiredMixin,CreateView):
    model = Teachers
    template_name = "teachers/add.html"
    form_class =  TeacherForm
    success_url = reverse_lazy('teachers_list')


@login_required
def teacher_list(request):
    context={}
    context['T_list'] = Teachers.objects.all()
    return render(request , 'teachers/list.html' ,context)




class TeachersUpdateView(LoginRequiredMixin,UpdateView):
    model = Teachers
    template_name = "teachers/add.html"
    form_class = TeacherForm
    success_url = reverse_lazy('teachers_list')
    pk_url_kwarg = 'id'


@login_required
def remove_teacher_list(request,id):
    Teacher_list = get_object_or_404(Teachers,id=id)
    Teacher_list.delete()
    return redirect('teacher_list')



@login_required(login_url='loginpage')
def student_register(request):
    if request.method == 'GET':
        context = {}
        context['forms'] = StudentRegisterForm()
        return render(request, 'student/student_register.html',context)


    elif request.method == 'POST':
        sr = StudentRegisterForm(request.POST)
        if sr.is_valid():
            user = sr.save(commit=False)
            user.is_staff=0
            user.is_student=1
            user.set_password(sr.cleaned_data.get('password'))
            user.save()
            return redirect('student_add')
        else:
            context = {}
            context['forms'] = sr
            return render(request, 'student/student_register.html',context)


@login_required(login_url='loginpage')
def student_add(request):
    context = {}
    context['student'] = User.objects.filter(is_student=1 , is_superuser=0)
    return render(request, 'student/student.html',context)


@login_required(login_url='loginpage')
def remove_student_list(request,id):
    student = get_object_or_404(User , pk=id)
    student.delete()
    return redirect('student_add')



@login_required(login_url='loginpage')
def staff_user_register(request):
    if request.method == 'GET':
        context = {}
        context['forms'] = StaffRegisterForm()
        return render(request, 'staff/staff_register.html' , context)


    elif request.method == 'POST':
        sur = StaffRegisterForm(request.POST)
        if sur.is_valid():
            user = sur.save(commit=False)
            user.is_student=0
            user.is_staff = 1
            user.set_password(sur.cleaned_data.get('password'))
            user.save()
            return redirect('staff_list')


        else:
            print(sur.errors)
            context = {}
            context['forms'] = sur
            return render(request, 'staff/staff_register.html' , context)




@login_required(login_url='loginpage')
def staff_list(request):
    context = {}
    context['staff'] = User.objects.filter(is_staff=1 , is_superuser=0)
    return render(request, 'staff/create_staff.html' , context)


@login_required(login_url='loginpage')
def remove_staff_list(request,id):
    student = get_object_or_404(User , pk=id)
    student.delete()
    return redirect('staff_list')




class AnnouncementsCreateView(CreateView,LoginRequiredMixin):
    model = MainAnnouncements
    template_name = "Announcement/add.html"
    form_class = AnnouncementsForm
    success_url = reverse_lazy('announcements_create')



def announcement_list(request):
    context = {}
    context['notice'] = MainAnnouncements.objects.all()
   
    return render(request, 'Announcement/list.html' , context)



class AnnouncementsUpdateView(UpdateView,LoginRequiredMixin):
    model = MainAnnouncements
    template_name = "Announcement/add.html"
    form_class = AnnouncementsForm
    success_url = reverse_lazy('announcement_list')
    pk_url_kwarg='id'



@login_required
def remove_announcements_list(request,id):
    remove_list = get_object_or_404(MainAnnouncements , id=id)
    remove_list.delete()
    return redirect('announcement_list')


