from django.shortcuts import render
from Prophet.models import Learner
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class LearnerCreateView(CreateView):
    model = Learner
    fields = ['name', 'email', 'roll']
    template_name = 'Prophet/learner_form.html'
    success_url = '/learner/'
    
class LearnerListView(ListView):
    model = Learner
    template_name = 'Prophet/learner_list.html'
    context_object_name = 'learners'
    
class LearnerDetailView(DetailView):
    model = Learner
    template_name = 'Prophet/learner_detail.html'
    context_object_name = 'learner'
    
class LearnerUpdateView(UpdateView):
    model = Learner
    fields = ['name', 'email', 'roll']
    template_name = 'Prophet/learner_form.html'
    success_url = '/learner/'
    
class LearnerDeleteView(DeleteView):
    model = Learner
    fields = ['name', 'email', 'roll']
    template_name = 'Prophet/learner_confirm_delete.html'
    success_url = '/learner/'
    

