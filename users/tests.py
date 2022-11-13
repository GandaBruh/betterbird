from django.test import TestCase
from urllib import response
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from users.views import index, aboutUs, logoutFunc,profile, viewProfile,likeBlog, cookieCoin, confirmCookie,homepage, members, loginPage, register, search, detail 
from users.models import Wallet, History, Blog, ReportBlog, CommentBlog, LikeBlog, ViewBlog, OwnedBlog, AccountUser,AccountOrganization,AccountAdmin
from django.contrib.auth.models import User

# Create your tests here.



class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_aboutUs_url_resolved(self):
        url = reverse('aboutUs')
        self.assertEquals(resolve(url).func, aboutUs)
    
    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_register_url_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
    
    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutFunc)

    def test_profile_url_resolved(self):
        url = reverse('viewProfile')
        self.assertEquals(resolve(url).func, viewProfile)

    def test_myprofile_url_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_likeBlog_url_resolved(self):
        url = reverse('viewProfile1')
        self.assertEquals(resolve(url).func, likeBlog)

    def test_cookieCoin_url_resolved(self):
        url = reverse('cookieCoin')
        self.assertEquals(resolve(url).func, cookieCoin)
    
    def test_confirmCookieCoin_url_resolved(self):
        url = reverse('confirmCookie', args=[0])
        self.assertEquals(resolve(url).func, confirmCookie)
    
    def test_homepage_url_resolved(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, homepage)
    
    def test_member_url_resolved(self):
        url = reverse('members')
        self.assertEquals(resolve(url).func, members)
    
    def test_search_url_resolved(self):
        url = reverse('blogpage')
        self.assertEquals(resolve(url).func, search)
    
    def test_detail_url_resolved(self):
        url = reverse('detail')
        self.assertEquals(resolve(url).func, detail)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.username = 'username'
        self.password = 'password'
        self.email = 'user@gmail.com'
        self.fname = 'first'
        self.lname = 'last'
        self.credentials = {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.fname,
            'last_name': self.lname}
        self.user = User.objects.create_user(**self.credentials)

        # self.cookie = 

        self.index_url = reverse('index')
        self.aboutUs_url = reverse('aboutUs')
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')
        self.viewProfile_url = reverse('viewProfile')
        self.profile_url = reverse('profile')
        self.likeBlog_url = reverse('viewProfile1')
        self.cookieCoin_url = reverse('cookieCoin')
        self.confirmCookie_url = reverse('confirmCookie', args=[0])
        self.homepage_url = reverse('homepage')
        self.members_url = reverse('members')
        self.blogpage_url = reverse('blogpage')
        self.detail_url = reverse('detail')


    def test_i(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_index_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')
    
    def test_aboutUs_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.aboutUs_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/aboutUs.html')

    def test_login_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'users/loginUser.html')
    
    def test_login_POST(self):
        # login incomplete
        credentials = {
            'username': 'user',
            'password': 'pass',
        }
        response = self.client.post(self.login_url, credentials, follow=True)

        self.assertFalse(response.context['user'].is_active)
        self.assertEquals(response.status_code, 400)
        self.assertTemplateUsed(response, 'users/loginUser.html')

    def test_login_POST_success(self):
        # login complete
        response = self.client.post(self.login_url, self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'users/homepage.html')

        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.login_url, {
            'username':self.username, 
            'password': self.password
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/loginUser.html')

    def test_register_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registerUserPpl.html')

    def test_profile_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/myProfile.html')

    def test_myProfile_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.viewProfile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/userProfile.html')

    def test_likeBlog_GET(self):
        pass

    # def test_cookieCoin_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.get(self.cookieCoin_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/cookieCoin.html')

    # def test_confirmCookie_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.get(self.confirmCookie_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/confirmCookie.html')

    def test_homepage_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')

    def test_members_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.members_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/members.html')

    # def test_blogpage_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.get(self.blogpage_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/search.html')

    def test_detail_GET(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/detail.html')
    