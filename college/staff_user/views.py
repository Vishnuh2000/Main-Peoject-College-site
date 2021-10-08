from django.shortcuts import render , redirect, get_object_or_404
from django.views.generic.list import ListView
from accounts.models import *
from accounts.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView , UpdateView , ListView , DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *



@login_required
def staff_home(request):
    return render(request , 'staff_home/home.html')



class SubjectCreateView(CreateView , LoginRequiredMixin):
    model = Subject
    template_name = "subject/create.html"
    form_class = SubjectForm
    success_url = reverse_lazy('subject_list_view')



class SubjectListView(ListView , LoginRequiredMixin):
    model = Subject
    template_name = "subject/list.html"
    context_object_name='object_list'

    def get_context_data(self, **kwargs):
        context = super(SubjectListView,self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context




class SubjectUpdateView(UpdateView , LoginRequiredMixin):
    model = Subject
    template_name = "subject/create.html"
    form_class = SubjectForm
    success_url = reverse_lazy('subject_list_view')
    pk_url_kwarg='id'



def subject_delete(request,id):
    remove_subject_list = get_object_or_404(Subject,id=id)
    remove_subject_list.delete()
    return redirect('subject_list_view')






class NotesCreateView(CreateView):
    model = Notes
    template_name = "notes/uploadfile.html"
    form_class = NotesForm
    success_url=reverse_lazy('notes_create_view')



class NotesListView(ListView):
    model = Notes
    template_name = "notes/notelist.html"


class NotesUpdateView(UpdateView):
    model = Notes
    template_name = "notes/uploadfile.html"
    form_class = NotesForm
    success_url = reverse_lazy('notes_list')
    pk_url_kwarg = 'id'

def notes_delete(request,id):
    remove_notes_list = get_object_or_404(Notes , id=id)
    remove_notes_list.delete()
    return redirect('notes_list')