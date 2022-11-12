from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from users.models import OwnedBlog, Blog, LikeBlog, AccountUser, AccountOrganization, ReportBlog
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse  # login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.


def index(request):
    return render(request, 'users/loginUser.html')


def aboutUs(request):
    return render(request, 'users/aboutUs.html')
# ----------------------------------------------------------------------#


def logoutFunc(request):
    logout(request)
    return render(request, 'users/loginUser.html', {
        'message': 'You are logged out.'
    })


def profile(request):
    userId = 1
    blog = OwnedBlog.objects.filter(
        user_id=request.user.id).values_list('blog_id', flat=True)
    blog1 = [1, 2, 3]
    return render(request, 'users/myProfile.html', {
        'blogs': blog1,
    })


def viewProfile(request):
    userId = 1
    blog = OwnedBlog.objects.filter(
        user_id=request.user.id).values_list('blog_id', flat=True)
    blog1 = [1, 2, 3]
    return render(request, 'users/userProfile.html', {
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

# Cookie coin - faii


all_cookie = [
    {'id': 1, 'cookies': 20, 'price': '2$'},
    {'id': 2, 'cookies': 50, 'price': '5$'},
    {'id': 3, 'cookies': 100, 'price': '10$'},
    {'id': 4, 'cookies': 500, 'price': '50$'},
    {'id': 5, 'cookies': 1000, 'price': '100$'},
    {'id': 6, 'cookies': 5000, 'price': '500$'},
]


def cookieCoin(request):
    context = {'cookies': all_cookie}
    return render(request, 'users/cookieCoin.html', context)


def confirmCookie(request, cookie_id):
    oneCookie = [c for c in all_cookie if c['id'] == cookie_id][0]
    context = {'cookies': oneCookie}
    return render(request, 'users/confirmCookie.html', context)

# ------------------------------------------------------------
# ----------------------chom---------------------------------


def homepage(request):
    blog1 = [1, 2, 3, 4]
    maxlen = len(blog1)
    return render(request, 'users/homepage.html', {
        'blogs': blog1,
        'maxlen': maxlen
    })


def members(request):
    return render(request, 'users/members.html')
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
                accountO = AccountOrganization.objects.create(
                    user=user, foundingDay=fday, phone=phone, address=address, orgName=orgName, country=country)

            elif (userType == "2"):
                bday = request.POST["bday"]
                country = request.POST["country"]
                address = request.POST["address"]
                phone = request.POST["phone"]
                accountU = AccountUser.objects.create(
                    user=user, birthday=bday, phone=phone, address=address, country=country)

        return HttpResponseRedirect(reverse("login"))

    return render(request, "users/registerUserPpl.html")


def reportBlog(request, id):
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
        return  HttpResponseRedirect(reverse("detail"))                                       
    return render(request, 'users/reportBlog.html', {
        'blogID' : blogID
    })

# ---------------------------fe-------------------------------


def detail(request):
    return render(request, 'users/detail.html')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # title_tag = Blog.objects.filter(title_tag_icontains = searched)
        return render(request, 'users/blogpageUser.html', {'searched': searched})
    else:
        return render(request, 'users/blogpageUser.html')
