from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import OwnedBlog, Blog, LikeBlog, AccountUser, CookieCoin, History, Wallet, AccountOrganization, ReportBlog, ViewBlog
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse  # login
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest 
from django.contrib.auth.models import User
from datetime import date as date_function
from random import randint
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import json

# Create your views here.

def index(request):
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    if not request.user.is_authenticated:
        return loginPage(request)
    return HttpResponseRedirect(reverse("homepage"))


def aboutUs(request):
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    return render(request, 'users/aboutUs.html', {
        'wallet' : wallet,
    })
# ----------------------------------------------------------------------#


def logoutFunc(request):
    logout(request)
    return render(request, 'users/loginUser.html', {
        'message': 'You are logged out.'
    })


def profile(request):
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    if not request.user.is_authenticated:
        return loginPage(request)
    userId=1
    user = AccountUser.objects.filter(user_id=request.user.id).first()
    if user:
        blogs = Blog.objects.filter(user_id=request.user.id).all()
        blog1 = [1,2,3]
        like = LikeBlog.objects.filter(user_id=request.user.id).values_list('blog_id', flat=True)
        print(like)
        print(blogs)
        return render(request, 'users/myProfile.html',{
            'blogs': blogs,
            'user': user,
            'wallet' : wallet,
            'like': like
        })
    else:
        user = AccountOrganization.objects.filter(user_id=request.user.id).first()
        blogs = Blog.objects.filter(user_id=request.user.id).all()
        blog1 = [1,2,3]
        print(blogs)
        return render(request, 'users/myProfile.html',{
            'blogs': blogs,
            'user': user,
            'wallet' : wallet
        })

def viewProfile(request):
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    userId=1
    print(request.user.id)
    
    blogs = Blog.objects.filter(user_id=request.user.id).values_list('pk', flat=True)
    blog1 = [1,2,3]
    
 
    return render(request, 'users/userProfile.html',{
        'blogs': blog1,
        'wallet': wallet,
    })

def likeBlog(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            id = data.get('blogId')
            like = data.get('like')
            if like:
                blog = Blog.objects.filter(pk=id).first()
                blog.like += 1
                blog.save()
                likeBlog = LikeBlog.objects.create(user=request.user, blog=blog)
                return JsonResponse({'status': 'like'})
            else:
                blog = Blog.objects.filter(pk=id).first()
                blog.like -= 1
                blog.save()
                likeBlog = LikeBlog.objects.filter(user=request.user, blog=blog).delete()
                return JsonResponse({'status': 'unlike'})

        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
   
        


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
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    return render(request, 'users/confirmPayment.html',{
        'wallet': wallet
    })
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

# ------------------------------------------------------------
# ----------------------chom---------------------------------


def homepage(request):
    try:
        userId = request.user.id
        wallet = Wallet.objects.get(user_id=userId)
    except Wallet.DoesNotExist:
        userId = None

    wallet = Wallet.objects.get(user_id=userId)
    blog = Blog.objects.filter(blogType=1, recommended=True).all()
    like = LikeBlog.objects.filter(user_id=request.user.id).values_list('blog_id', flat=True)
    print(like)
    maxlen = len(blog)
    return render(request, 'users/homepage.html', {
        'blogs': blog,
        'like': like,
        'maxlen': maxlen,
        'wallet' : wallet,
    })


def members(request):
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    return render(request,'users/members.html' , {
        'wallet':wallet
    })

def createblog(request):
    global userID
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        title = request.POST['title']
        introduction = request.POST['introduction']
        detail = request.POST['detail']
        tag = request.POST['tag']
        date1 = request.POST['date1']
        image = request.FILES['image']
        expectCookies = request.POST['expectCookies']

        blog = Blog.objects.create(user=user,title=title,
        introduction=introduction,detail=detail,
        tag=tag,date1=date1,image=image,donate=0,blogType=0,recommended=False,
        like=0,expectCookies=expectCookies)

        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'users/createBlog.html', {
        'wallet':wallet
    })

# ---------------------------------------------------------------
# -------------------------safe---------------------------------



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


def register(request):  # register
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmPassword = request.POST["cpassword"]
        userType = request.POST["userType"]
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        email = request.POST["email"]

        if (password == confirmPassword):
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=firstname, last_name=lastname)

            if (userType == "1"):
                orgName = request.POST["orgName"]
                fday = request.POST["fday"]
                country = request.POST["country"]
                address = request.POST["address"]
                phone = request.POST["phone"]
                image = request.POST["image"]
                accountO = AccountOrganization.objects.create(
                    user=user, foundingDay=fday, phone=phone, address=address, orgName=orgName, country=country, image=image)

            elif (userType == "2"):
                bday = request.POST["bday"]
                country = request.POST["country"]
                address = request.POST["address"]
                phone = request.POST["phone"]
                image = request.POST["image"]
                accountU = AccountUser.objects.create(
                    user=user, birthday=bday, phone=phone, address=address, country=country, image=image)


            wallet = Wallet.objects.create(user=user, balanceCookie=0)
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/registerUserPpl.html")


def reportBlog(request, id):
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    blogID = id
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        blog = Blog.objects.get(pk=id)
        reason1 = request.POST.get("reason1", False)
        reason2 = request.POST.get("reason2", False)
        reason3 = request.POST.get("reason3", False)
        reason4 = request.POST.get("reason4", False)
        reason5 = request.POST.get("reason5", False)
        reason6 = request.POST.get("reason6", False)
        otherReason = request.POST.get("otherReason")
        reportBlog = ReportBlog.objects.create(reason1=reason1, reason2=reason2, reason3=reason3,
                                               reason4=reason4, reason5=reason5, reason6=reason6,
                                               otherReason=otherReason, user=user,
                                               blog=blog)
        return HttpResponseRedirect(reverse("detail", args=[id]))
    return render(request, 'users/reportBlog.html', {
        'blogID': blogID, 
        'wallet': wallet, 
    })
#------------------------------------------------------------
#---------------------------fe-------------------------------


    

def donate(request):
    global userID
    try:
        user_id = request.user.id
        wallet = Wallet.objects.get(user_id=user_id)
    except Wallet.DoesNotExist:
        user_id = None

    if request.method == "POST":
        userID=request.user.id
        cookie = request.POST["cookie"]
        transactionCode = randint(1, 100000)

        history = History.objects.filter(userID=request.user.id )
        account = History.objects.create(
            userID=userID, cookie=cookie, transactionCode=transactionCode)
        
        wallet = Wallet.objects.get(user_id=request.user.id)
        wallet.balanceCookie -= int(cookie)
        wallet.save()
        return HttpResponseRedirect(reverse("confirmPayment"))
    return render(request, 'users/blogpageUser.html',{
        'wallet' : wallet,
        'history' : history,
    })



def searchBar(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        if searched:
            blogs = Blog.objects.filter(title__contains=searched)
            return render(request, 'users/searchfor.html', {'blogs': blogs})
        else:
            print("No information to show")
            return render(request, 'users/searchfor.html', {})



def BlogView(request):
    blogs = Blog.objects.filter(blogType = 1).all()
    like = LikeBlog.objects.filter(user_id=request.user.id).values_list('blog_id', flat=True)
    print(like)
    return render(request, 'users/blogpageUser.html', {'blogs':blogs, 'like':like})

def DetailView(request, detail_id):
    blog = Blog.objects.get(id = detail_id)
    viewed = ViewBlog.objects.filter(user_id=request.user.id).values_list('blog_id', flat=True)
    if detail_id not in viewed:
        views = ViewBlog.objects.create(user=request.user, blog=blog)
        blog.views += 1
        blog.save()
   
    return render(request,'users/detail.html', {'blog':blog})