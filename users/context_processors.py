
from users.models import OwnedBlog, Blog, LikeBlog, AccountUser, CookieCoin, History, Wallet, AccountOrganization, ReportBlog, ViewBlog
from django.shortcuts import render
def setup_user(request):
    if not request.user.is_authenticated:
        return {}
    user = AccountUser.objects.filter(user_id=request.user.id).first()
    if user:
 
        return{
            'userlayout': user,
        }
    else:
        user = AccountOrganization.objects.filter(user_id=request.user.id).first()
        return {
            'userlayout': user,
        }
    