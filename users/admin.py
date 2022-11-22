from django.contrib import admin
from users.models import LikeBlog, AccountUser, AccountOrganization, Blog ,ReportBlog, CookieCoin, Wallet, History, ViewBlog
# Register your models here.
admin.site.register([LikeBlog, Blog, AccountUser, AccountOrganization, ReportBlog, CookieCoin, Wallet, History, ViewBlog])


 