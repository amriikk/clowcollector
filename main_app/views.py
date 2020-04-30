from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Clow



# Define the home view
def home(request):
  return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

class ClowList(ListView):
  model = Clow

  def get_queryset(self):
    return Clow.objects.all()

class ClowDetail(DetailView):
  model = Clow

class ClowCreate(CreateView):
  model = Clow
  fields = '__all__' #includes all fields for Clow

class ClowUpdate(UpdateView):
  model = Clow
  fields = ['sign', 'description', 'magic']

class ClowDelete(DetailView):
  model = Clow
  success_url = '/clows/'