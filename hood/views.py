from django.shortcuts import render,get_object_or_404
from .models import Neighbourhood

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request,Neighbourhood_id):
    posts = Post.objects.filter(Neighbourhood=Neighbourhood_).all()
    print(posts)
    return render(request,'index.html',{"posts":posts})

def single_photo(request,post_id):
    photo = Post.objects.get(id=post_id)
    return render(request,'photo_details.html',
    {'photo':photo})
    