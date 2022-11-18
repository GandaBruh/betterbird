from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now



# Create your models here.

class CookieCoin(models.Model):
    cookie = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.cookie}"

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    balanceCookie = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user}"

    # def userWallet():
    #     hist_cookie = History.objects.all()
    #     total = hist_cookie.cookie + Wallet.balanceCookie
    #     return total


class History(models.Model):
    userID = models.IntegerField(default=0)
    #amount = models.IntegerField(default=0) # จำนวนที่ใช้ไป relate w/ currency
    slip = models.CharField(max_length=9999, null=True, blank=True)
    transactionCode = models.CharField(max_length=9999)
    historyType =  models.BooleanField(default=False)
    currency = models.BooleanField(default=False) # 0 = cash, 1 = cookie
    date = models.DateTimeField(null=True)#auto_now_add=True
    time = models.TimeField(default=datetime.time(16, 00))
    cookie = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.userID}"

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=9999)
    introduction = models.CharField(max_length=9999)
    detail = models.CharField(max_length=9999)
    tag = models.CharField(max_length=9999)
    date1 = models.DateField()
    image = models.ImageField(upload_to='users/static/images')
    donate = models.IntegerField(default=0)
    blogType = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    expectCookies = models.IntegerField()


class ReportBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    reason1 = models.BooleanField("reason1", default=False)
    reason2 = models.BooleanField("reason2", default=False)
    reason3 = models.BooleanField("reason3", default=False)
    reason4 = models.BooleanField("reason4", default=False)
    reason5 = models.BooleanField("reason5", default=False)
    reason6 = models.BooleanField("reason6", default=False)
    otherReason = models.CharField(max_length=256)


class CommentBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    detail = models.CharField(max_length=5000)


class ViewBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class OwnedBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class LikeBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class AccountUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    phone = models.CharField(max_length=256)
    address = models.CharField(max_length=9999)
    country = models.CharField(max_length=9999)
    likeCount = models.IntegerField(default=0)
    viewCount = models.IntegerField(default=0)


class AccountOrganization(models.Model):
    orgName = models.CharField(max_length=9999, default="1")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foundingDay = models.DateField()
    phone = models.CharField(max_length=9999)
    address = models.CharField(max_length=9999)
    country = models.CharField(max_length=9999)
    likeCount = models.IntegerField(default=0)
    viewCount = models.IntegerField(default=0)


class AccountAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=9999)
    phone = models.CharField(max_length=9999)
    tag = models.CharField(max_length=9999)

