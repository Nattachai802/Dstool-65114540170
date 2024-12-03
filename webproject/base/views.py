from django.shortcuts import render
from django.views.generic import UpdateView
from base.models import *
from django.urls import reverse_lazy
# Create your views here.

def course_list(request):
    c = course.objects.all()
    return render(request,'list.html',{'course':c})

class updateview(UpdateView):
    template_name = 'update.html'
    model = course
    success_url = reverse_lazy('list')
    fields = ['cid','name']
