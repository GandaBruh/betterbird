from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from users.models import OwnedBlog, Blog, LikeBlog, AccountUser
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse  # login
from django.http import HttpResponseRedirect 
from .forms import RegisterForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
# Create your views here.
def index(request):
    return render(request, 'users/loginUser.html')

def aboutUs(request):
    return render(request, 'users/aboutUs.html')
#----------------------------------------------------------------------#

def logoutFunc(request):
    logout(request)
    return render(request, 'users/loginUser.html', {
        'message': 'You are logged out.'
    })

def profile(request):
    userId=1
    blog = OwnedBlog.objects.filter(user_id=request.user.id).values_list('blog_id', flat=True)
    blog1 = [1,2,3]
    return render(request, 'users/myProfile.html',{
        'blogs': blog1,
    })

def viewProfile(request):
    userId=1
    blog = OwnedBlog.objects.filter(user_id=request.user.id).values_list('blog_id', flat=True)
    blog1 = [1,2,3]
    return render(request, 'users/userProfile.html',{
        'blogs': blog1,
    })

def likeBlog(request):
    id = request.POST['id']
    
    blog = Blog.objects.filter(pk=id).first()
    like = True
    if like:
        blog.like += 1
        blog.save()
        likeBlog = LikeBlog(user=request.user, blog=blog)
    return

#Cookie coin - faii

all_cookie = [
    {'id': 1, 'cookies': 20 , 'price' : '2$'},
    {'id': 2, 'cookies': 50 , 'price' : '5$'},
    {'id': 3, 'cookies': 100, 'price' : '10$'},
    {'id': 4, 'cookies': 500, 'price' : '50$'},
    {'id': 5, 'cookies': 1000, 'price' : '100$'},
    {'id': 6, 'cookies': 5000, 'price' : '500$'},
]

def cookieCoin(request):
    context={'cookies': all_cookie}
    return render(request, 'users/cookieCoin.html', context)

def confirmCookie(request, cookie_id):
    oneCookie = [c for c in all_cookie if c['id'] == cookie_id][0]
    context = {'cookies': oneCookie}
    return render(request, 'users/confirmCookie.html', context)

#------------------------------------------------------------
#----------------------chom---------------------------------

def homepage(request):
    blog1 = [1,2,3,4]
    maxlen = len(blog1)
    return render(request, 'users/homepage.html',{
        'blogs': blog1,
        'maxlen':maxlen
    })

def members(request):
    return render(request,'users/members.html' )
#---------------------------------------------------------------
#-------------------------safe---------------------------------
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'users/loginUser.html', {
                'message': 'Invalid credentials.'
            })

    return render(request, 'users/loginUser.html')

# Create your views here.


def register(response):  # register
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse("login"))
    else:
        form = RegisterForm()

    return render(response, "users/registerUserPpl.html", {"form": form})
#------------------------------------------------------------
#---------------------------fe-------------------------------

class BlogView(ListView):
    model = Blog
    template_name = 'users/blogpageUser.html'

class DetailView(DetailView):
    model = Blog
    template_name = 'users/detail.html'

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            blogs = Blog.objects.filter(title__icontains=query)
            return render(request, 'users/searchfor.html', {'blogs':blogs})
        else:
            print("No information to show")
            return render(request, 'users/searchfor.html', {})

    
def detail(request):
    return render(request, 'users/detail.html')
