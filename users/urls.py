from django.urls import path, include
from . import views
from django.conf .urls.static import static
from django.conf import settings
from .views import BlogView, DetailView



urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('login/', views.loginPage, name='login'),  # login
    path("register/", views.register, name="register"),
    path('logout', views.logoutFunc, name='logout'),
    path('profile/<int:id>', views.viewProfile, name="viewProfile"),
    path('myProfile/', views.profile, name="profile"),
    path('profile/likeBlog', views.likeBlog, name="viewProfile1"),
    path('cookieCoin/', views.cookieCoin, name='cookieCoin'),
    path('cookieCoin/<int:cookie_id>', views.confirmCookie, name='confirmCookie'),
    path('homepage/', views.homepage, name='homepage'),
    path('members/', views.members, name='members'),
    path('createblog/', views.createblog, name='createBlog'),
    path('confirmPayment/', views.confirmPayment, name='confirmPayment'),
    path('blogpage/', views.BlogView, name='blogpage'),
    path('detail/<int:detail_id>', views.DetailView, name='detail'),
    path('search/', views.searchBar, name='search'),
    path('report/<int:id>', views.reportBlog, name='report'),
    path('donate/<int:id>', views.donate, name='donate'),
    path('likeBlog', views.likeBlog, name='likeBlog'),
    path('homepageadmin/', views.homepageadmin, name='homepageadmin'),
    path('detailadmin/<int:detail_id>', views.detailadmin, name='detailadmin'),
    path('verify/<int:id>',views.verify, name = 'verify'),
     path('recommended/<int:id>',views.recommended, name = 'recommended'),
    path('reportPageAdmin/', views.reportPageAdmin, name='reportPageAdmin'),
    path('notVerifiedPageAdmin/', views.notVerifiedPageAdmin,name='notVerifiedPageAdmin'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
