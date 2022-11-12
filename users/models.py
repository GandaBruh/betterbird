from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class History(models.Model):
    amount = models.IntegerField(default=0)
    slip = models.CharField(max_length=9999)
    transactionCode = models.CharField(max_length=9999)
    historyType = models.BooleanField(default=False)
    currency = models.BooleanField(default=False)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=9999)
    introduction = models.CharField(max_length=9999)
    detail = models.CharField(max_length=9999)
    tag = models.CharField(max_length=9999)
    date = models.DateField()
    image = models.CharField(max_length=256)
    donate = models.IntegerField(default=0)
    blogType = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    expectCookies = models.IntegerField(default=0)


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
