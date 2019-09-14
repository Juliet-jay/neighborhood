from django.shortcuts import render,get_object_or_404
from .models import Neighbourhood

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request,Neighbourhood_id):
    Posts = Post.objects.filter(Neighbourhood=Neighbourhood_).all()
    print(posts)
    return render(request,'index.html',{"posts":posts})