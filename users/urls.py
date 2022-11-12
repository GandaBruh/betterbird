from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('login/', views.loginPage, name='login'),  # login
    path("register/", views.register, name="register"),
    path('logout', views.logoutFunc, name='logout'),
    path('profile/', views.viewProfile, name="viewProfile"),
    path('myProfile/', views.profile, name="profile"),
    path('profile/likeBlog', views.likeBlog, name="viewProfile1"),
    path('cookieCoin/', views.cookieCoin, name='cookieCoin'),
    path('cookieCoin/<int:cookie_id>', views.confirmCookie, name='confirmCookie'),
    path('homepage/', views.homepage, name='homepage'),
    path('members/', views.members, name='members'),
    path('blogpage/', views.search, name='blogpage'),
    path('detail/', views.detail, name='detail'),
    path('report/<int:id>', views.reportBlog, name='report'),
]
