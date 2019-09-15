from django.shortcuts import render,get_object_or_404
from .models import Neighbourhood

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request,Neighbourhood_id):
    posts = Post.objects.filter(Neighbourhood=Neighbourhood_).all()
    print(posts)
    return render(request,'home.html',{"posts":posts})

def single_photo(request,post_id):
    photo = Post.objects.get(id=post_id)
    return render(request,'photo_details.html',
    {'photo':photo})
    
def search_results(request):
    if 'businesses' in request.GET and request.GET["businesses"]:
        search_term = request.Get.get("businesses")
        searched_businesses = Business.search_by_neighbourhood(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"message":message,"businesses":searched_businesses})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
    
    
    