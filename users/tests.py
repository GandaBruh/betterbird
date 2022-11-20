from django.test import TestCase
from urllib import response
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from users.views import index, aboutUs, logoutFunc,profile, viewProfile,likeBlog, cookieCoin, confirmCookie,homepage, members, loginPage, register, createblog, searchBar, reportBlog, confirmPayment, BlogView, DetailView, LikeBlog  
from users.models import Wallet, History, Blog, ReportBlog, CookieCoin, CommentBlog, LikeBlog, ViewBlog, OwnedBlog, AccountUser,AccountOrganization,AccountAdmin
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
        url = reverse('viewProfile', args=[0])
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
    
    def test_createBlog_url_resolved(self):
        url = reverse('createBlog')
        self.assertEquals(resolve(url).func, createblog)
    
    def test_confirmPayment_url_resolved(self):
        url = reverse('confirmPayment')
        self.assertEquals(resolve(url).func, confirmPayment)

    def test_blogpage_url_resolved(self):
        url = reverse('blogpage')
        self.assertEquals(resolve(url).func, BlogView)
    
    def test_confirmPayment_url_resolved(self):
        url = reverse('detail', args=[0])
        self.assertEquals(resolve(url).func, DetailView)

    def test_search_url_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, searchBar)
    
    def test_report_url_resolved(self):
        url = reverse('report', args=[0])
        self.assertEquals(resolve(url).func, reportBlog)
    
    def test_likeBlog_url_resolved(self):
        url = reverse('likeBlog')
        self.assertEquals(resolve(url).func, likeBlog)

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
        self.viewProfile_url = reverse('viewProfile', args=[0])
        self.profile_url = reverse('profile')
        self.likeBlog_url = reverse('viewProfile1')
        self.cookieCoin_url = reverse('cookieCoin')
        self.confirmCookie_url = reverse('confirmCookie', args=[0])
        self.homepage_url = reverse('homepage')
        self.members_url = reverse('members')
        self.createBlog_url = reverse('createBlog')
        self.confirmPayment_url = reverse('confirmPayment')
        self.blogpage_url = reverse('blogpage')
        self.detail_url = reverse('detail', args=[0])
        self.search_url = reverse('search')
        self.report_url = reverse('report', args=[0])
        self.likeBlog_url = reverse('likeBlog')

    def test_i(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_index_GET(self):
        self.client.login(username=self.username, password=self.password)
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')
    
    def test_aboutUs_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        wallet = Wallet.objects.create(user=user, balanceCookie=0)
        login = self.client.login(username="CCC", password="111")
        # self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('aboutUs'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/aboutUs.html')

    def test_login_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
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
        
        wallet = Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.post(self.login_url, self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'users/homepage.html')

        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.login_url, {
            'username':self.username, 
            'password': self.password, 
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/loginUser.html')

    def test_create_blog_POST(self):
        user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        with open('users/static/images/tee.jpg','rb') as img:
            response = self.client.post(reverse('createBlog'), {'title':'title', 'introduction': 'introduction', 'detail':'example test detail', 'tag':'example tag', 'date1':'2022-11-11', 'image':img, 'expectCookies': 0})
        self.assertEqual(response.status_code, 302)

    def test_register_POST_usertype1(self):
        with open('users/static/images/tee.jpg','rb') as img:
            response = self.client.post(reverse('register'), {
                'username': 'AAA', 'password': '123456AAA', 'cpassword': '123456AAA', 'userType': '1', 
                'fname': "AAAA", 'lname': 'BBBBb', 'email': 'sec@example.com', 'orgName':'Fondations',
                'fday': '2022-01-20', 'country':'country test', 'address': 'address 66/7', 'phone': '0547877979',
                'image': img})
            self.assertEqual(response.status_code, 302)

    def test_register_POST_usertype2(self):
        with open('users/static/images/tee.jpg','rb') as img:
            response = self.client.post(reverse('register'), {
                'username': 'AAA', 'password': '123456AAA', 'cpassword': '123456AAA', 'userType': '2', 
                'fname': "AAAA", 'lname': 'BBBBb', 'email': 'sec@example.com', 
                'bday': '2022-01-20', 'country':'country test', 'address': 'address 66/7', 'phone': '0547877979',
                'image': img})
        self.assertEqual(response.status_code, 302)
 
    def test_register_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_myProfile_GET(self):
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.post(self.profile_url, {
            'username': self.username, 'password': self.password, 
            'fname': self.fname, 'lname': self.lname, 
            'email': self.email, 'phone': '0547877979'})
        self.client.login(username=self.username, password=self.password)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')

    # def test_likeBlog_GET(self):
    #     pass

    def test_cookies_confirm(self):
        wallet = Wallet.objects.create(user=self.user, balanceCookie=0)
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('confirmCookie', args=[1]), {'time': '06:00:00.00000', 'date':'2022-02-11', 'slip':'', 'cookie':500, 'price':50 })
                                                                
        self.assertEqual(response.status_code, 302)

    def test_cookies_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        cookie = CookieCoin.objects.create(cookie=10, price=10)
        login = self.client.login(username="CCC", password="111")
        wallet = Wallet.objects.create(user=user, balanceCookie=0)
        response = self.client.get(reverse('confirmCookie', args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_confirmPayment_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        wallet = Wallet.objects.create(user=user, balanceCookie=10)
        login = self.client.login(username="CCC", password="111")
        response = self.client.get(reverse('confirmPayment'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/confirmPayment.html')

    def test_homepage_GET(self):
        Wallet.objects.create(user=self.user, balanceCookie=0)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')

    # def test_homepage_POST(self):
    #     response = self.client.post(self.homepage_url)
    #     self.assertEquals(response.status_code, 400)
    #     self.assertTemplateUsed(response, 'users/loginUser.html')

    def test_members_GET(self):
        self.client.login(username=self.username, password=self.password)
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.get(self.members_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/members.html')

    # def test_blogpage_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.get(self.blogpage_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/search.html')

    # def test_detail_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     response = self.client.get(self.detail_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/detail.html')
    