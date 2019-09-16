from django.shortcuts import render,get_object_or_404,redirect
from .models import Neighbourhood,Business,Post,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,PostForm,BusinessForm,NeighbourhoodForm
from django.contrib.auth.models import User
# Create your views here.
def welcome(request):
    
    return render(request, 'welcome.html')

def home(request):
    posts = Post.objects.all()
    print(posts)
    return render(request,'home.html',{"posts":posts})

def single_photo(request,post_id):
    photo = Post.objects.get(id=post_id)
    return render(request,'photo_details.html',
    {'photo':photo})
    
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.Get.get("business")
        searched_businesses = Business.search_by_neighbourhood(search_term)
        message = search_term
        
        return render(request, 'search-results.html',{"message":message,"businesses":searched_businesses})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search-results.html',{"message":message})
    
    

def neighbourhoods(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods.html',{'neighbourhood':neighbourhood})

def business(request):
    
    businesses = Business.get_businesses()
    return render(request, 'business.html',{"businesses":businesses})

    
@login_required(login_url = '/accounts/login')
def create_profile(request):
    current_user = request.user
    profiles = Profile.objects.filter(user=current_user).count()
    
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        neighForm=NeighbourhoodForm(request.POST,instance=request.user.profile.neighbourhood)
        
        if form.is_valid() and neighForm.is_valid():
            
            k = form.save(commit=False)
            k.user = current_user
            
            n=neighForm.save(commit=False)
            n.user=current_user
            k.neighbourhood=n.user.profile.neighbourhood
            
            
            n.save()
            k.save()
            return redirect(profile)
           
    
    else:
        form = ProfileForm(instance=request.user.profile)
        neighForm=NeighbourhoodForm(instance=request.user.profile.neighbourhood)
    return render(request, 'profile_form.html',{"form":form,"neighForm":neighForm})
    

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    
    try:
        profile = Profile.objects.get(user=current_user)
        
        title = current_user.username
        
        # pics = Post.objects.filter(user=request.user.profile.id).all()
        
    except:
        
        title = current_user.username
        
        pics = Post.objects.filter(user=request.user.profile.id).all()
        
    return render(request, 'profile.html', {"title": title, "profile":profile})

@login_required(login_url='/accounts/login')
def post(request):
    current_user = request.user
    
    # posts = Post.objects.filter(user=current_user).count()
        
    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            k = form.save(commit=False)
            k.user = current_user
            k.save()
            return redirect('home')
        
    else:
        form = PostForm()
    return render(request, 'post_form.html', {"form": form})



@login_required(login_url='/accounts/login')
def create_business(request):
    current_user = request.user
    if request.method == 'POST':
        
        form = BusinessForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            k = form.save(commit=False)
            k.user = current_user
            k.neighbourhood=current_user.profile.neighbourhood
            k.save()
            return redirect('home')
        
    else:
        form = BusinessForm()
    return render(request, 'business_form.html', {"form": form})


            
    

        
    