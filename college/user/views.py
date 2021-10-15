from django.shortcuts import render , get_object_or_404 , redirect , HttpResponseRedirect
from owner.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView ,ListView ,UpdateView
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from staff_user.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string




def Home(request):
    context={}
    context['notice'] = MainAnnouncements.objects.all()
    return render(request , 'user_home/home.html' , context)


def NoticeDetails(request,id):
    context={}
    context['notice'] = get_object_or_404(MainAnnouncements , pk=id)
    return render(request , 'user_home/notice.html' , context)


@login_required
def About(request):
    return render(request , "user_home/about.html")


@login_required
def department_view(request):
    context={}
    context['departments'] = Department.objects.all()
    return render(request , 'department/Home_view.html' , context)


@login_required
def department_details(request,id):
    context = {}
    context['department'] = get_object_or_404(Department,id=id)
    context['teachers'] = Teachers.objects.filter(Name=context['department'])
    return render(request , 'department/details.html' , context)



@login_required
def Activity_view(request):
    context={}
    context['activity'] = Activity.objects.all()
    return render(request , 'activity/view.html' , context)


@login_required
def Activity_details(request,id):
    context={}
    context['activities'] = get_object_or_404(Activity , id=id)
    return render(request , 'activity/details.html' , context)


@login_required
def Factility_view(request):
    context={}
    context['Facility'] = Facilities.objects.all()
    return render(request , 'facility/view.html' , context)


@login_required
def Facility_details(request,id):
    context={}
    context['facilities'] = get_object_or_404(Facilities , id=id)
    return render(request , 'facility/details.html' , context)



def ContactCreateView(request):
    if request.method == 'GET':
        context={}
        context['form'] = ContactForm()
        return render( request , 'user_home/contact.html' , context )

    elif request.method == 'POST':
        cf = ContactForm(request.POST or None)
        if cf.is_valid():
            saveform = cf.save(commit=False)
            saveform.user = request.user
            saveform.save()
            return redirect('contact')

        else:
            print(cf.errors)
            context={}
            context['form'] = cf
            return render( request , 'user_home/contact.html' , context )

   

def error_404(request ,exception):
    data = {}
    return render(request ,'error/error404.html' , data)


def student_home(request):
    context={}
    context['department'] = Department.objects.all()[:5]
    return render(request , 'student/notes_dpt.html',context)


def student_subject(request,id):
    context={}
    context['course'] = get_object_or_404(Department,id=id)
    context['subject1'] = Subject.objects.filter(name=context['course'] , semester=1)
    context['subject2'] = Subject.objects.filter(name=context['course'] , semester=2)
    context['subject3'] = Subject.objects.filter(name=context['course'] , semester=3)
    context['subject4'] = Subject.objects.filter(name=context['course'] , semester=4)
    context['subject5'] = Subject.objects.filter(name=context['course'] , semester=5)
    context['subject6'] = Subject.objects.filter(name=context['course'] , semester=6)
    return render(request , 'student/note_sub.html', context)



def studentFile_download(request,id):
    context={}
    context['subject'] = get_object_or_404(Subject,id=id)
    context['notes'] = Notes.objects.filter(sub=context['subject'])
    return render(request , 'student/download.html' , context)








