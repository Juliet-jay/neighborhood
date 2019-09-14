from django.shortcuts import render,get_object_or_404
from .models import Neighbourhood

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')