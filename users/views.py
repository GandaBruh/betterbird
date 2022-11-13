from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from users.models import OwnedBlog, Blog, LikeBlog, AccountUser, CookieCoin, History, Wallet
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse  # login
from django.http import HttpResponseRedirect 
from .forms import RegisterForm
from django.contrib.auth.models import User
from random import randint

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

#Cookie coin - faiinarak

def cookieCoin(request):
    global user_id
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    history = History.objects.filter(userID=request.user.id )
    cookieCoin = CookieCoin.objects.all()
    return render(request, 'users/cookieCoin.html',{
        'cookieCoin' : cookieCoin, 
        'wallet' : wallet,
        'history' : history, 
    })


def confirmCookie(request, cookie_id):
    global userID
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    if request.method == "POST":
        userID=request.user.id
        time = request.POST['time']
        slip = request.POST["slip"]
        date = request.POST["date"]
        cookie = request.POST["cookie"]
        price = request.POST["price"]
        transactionCode = randint(1, 100000)

        account = History.objects.create(
            time=time, slip=slip, date=date, userID=userID, cookie=cookie, price=price, transactionCode=transactionCode)
        
        wallet = Wallet.objects.get(user_id=request.user.id)
        wallet.balanceCookie += int(cookie)
        wallet.save()


        return HttpResponseRedirect(reverse("confirmPayment"))
    cookieCoins = CookieCoin.objects.get(pk=cookie_id)
    return render(request, 'users/confirmCookie.html',{
        'cookieCoin' : cookieCoins, 
        'wallet' : wallet,
    })

def confirmPayment(request):
    return render(request, 'users/confirmPayment.html')
    # cookieCoins = CookieCoin.objects.get(pk=cookie_id)
    # return render(request, 'users/confirmCookie.html',{
    #     'cookieCoin': cookieCoins
    # })

    # if request.method == 'POST':
    #     cookieCoin = CookieCoin.objects.get(pk=cookie_id)
    #     user = User.objects.get(pk=request.user.id)
        
    #     check = History.objects.filter(user=user, cookieCoin=cookieCoin).first()
    #     if check is None:
    #         history = History.objects.create(user=user, cookieCoin=cookieCoin)
    #         return cookieCoin(request)

    #     else: 
    #         return render(request, 'course/cookieCoin.html', {
    #             'cookieCoin' : cookieCoin,
    #             'history': check is not None
    #         }, status=400)  
    # else:
    #     cookieCoin = CookieCoin.objects.get(pk=cookie_id)
    #     user = User.objects.get(pk=request.user.id)
    #     check = History.objects.filter(user=user, cookieCoin=cookieCoin).first()

    #     return render(request, 'course/cookieCoin.html', {
    #         'cookieCoin' : cookieCoin, 
    #         'history': check is not None
    #     }, status=400) 

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

#---------------------------fe-------------------------------
def detail(request):
    return render(request, 'users/detail.html')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # title_tag = Blog.objects.filter(title_tag_icontains = searched)
        return render(request, 'users/blogpageUser.html', {'searched':searched})
    else:
        return render(request, 'users/blogpageUser.html')