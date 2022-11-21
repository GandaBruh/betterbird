from django.test import TestCase
from urllib import response
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from users.views import index, aboutUs, logoutFunc,profile, viewProfile,likeBlog, cookieCoin, confirmCookie,homepage, members, loginPage, register, createblog, searchBar, reportBlog, confirmPayment, BlogView, DetailView, LikeBlog ,homepageadmin,detailadmin,verify,recommended,reportPageAdmin,notVerifiedPageAdmin
from users.models import Wallet, History, Blog, ReportBlog, CookieCoin, CommentBlog, LikeBlog, ViewBlog, OwnedBlog, AccountUser,AccountOrganization,AccountAdmin
from django.contrib.auth.models import User
import json

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

    def test_homepageadmin_url_resolved(self):
        url = reverse('homepageadmin')
        self.assertEquals(resolve(url).func, homepageadmin)

    def test_detailadmin_url_resolved(self):
        url = reverse('detailadmin',args=[0])
        self.assertEquals(resolve(url).func, detailadmin)

    def test_verify_url_resolved(self):
        url = reverse('verify',args=[0])
        self.assertEquals(resolve(url).func, verify)

    def test_recommended_url_resolved(self):
        url = reverse('reccomended',args=[0])
        self.assertEquals(resolve(url).func, recommended)
    
    def test_homepageadmin_url_resolved(self):
        url = reverse('reportPageAdmin')
        self.assertEquals(resolve(url).func, reportPageAdmin)

    def test_notVerifiedPageAdmin_url_resolved(self):
        url = reverse('notVerifiedPageAdmin')
        self.assertEquals(resolve(url).func, notVerifiedPageAdmin)

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
        self.homepageadmin_url = reverse('homepageadmin')
        self.verify_url = reverse('verify', args=[0])

        #self.donate_url = reverse('donate',arg=[0])
        #self.detailadmin_url = reverse('detailadmin', arg=[0])

     
# ---------------------------------index--------------------------#

    def test_i(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 302)

    def test_index_GET(self):
        self.client.login(username=self.username, password=self.password)
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')

    def test_index_POST(self):
        response = self.client.post(self.homepage_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.homepage_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')
    
# --------------------------------aboutus--------------------------------#
    
    def test_aboutUs_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        wallet = Wallet.objects.create(user=user, balanceCookie=0)
        login = self.client.login(username="CCC", password="111")
        # self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('aboutUs'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/aboutUs.html')
    
# ----------------------------------logout--------------------------------#

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# --------------------------------profile--------------------------------#

    def test_profile_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/loginUser.html')

    def test_profile_POST(self):
        response = self.client.post(self.profile_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.profile_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# ---------------------------------viewprofile---------------------------------#

    # def test_viewProfile_GET(self):
    #     user = User.objects.create_user(username="CCC", password="111")
    #     login = self.client.login(username="CCC", password="111")
    #     response = self.client.get(reverse('viewProfile'))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/viewProfile.html')

    def test_viewProfile_POST(self):
        response = self.client.post(self.profile_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.viewProfile_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# ------------------------------------likeblog--------------------------#

    def test_like_POST(self):
        blog = Blog.objects.create()
        user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {"like":True, "blogId":1}
        response = self.client.post('/likeBlog', headers=headers, content_type="application/json", data = json.dumps(data), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEquals(response.status_code, 200)

    def test_unlike_POST(self):
        blog = Blog.objects.create()
        user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {"like":False, "blogId":1}
        response = self.client.post('/likeBlog', headers=headers, content_type="application/json", data = json.dumps(data), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEquals(response.status_code, 200)

    def test_like_get(self):
        blog = Blog.objects.create()
        user = User.objects.create_user(username="CCC",password="111")
        login = self.client.login(username="CCC", password="111")
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        
        response = self.client.get('/likeBlog', headers=headers, content_type="application/json", HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEquals(response.status_code, 400)

    def test_like_fail(self):
        blog = Blog.objects.create()
        user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        headers = {'X-Requested-With': 'sdafadsf'}
        data = {"like":True, "blogId":1}
        response = self.client.post('/likeBlog', headers=headers, content_type="application/json", data = json.dumps(data))
        self.assertEquals(response.status_code, 400)

# --------------------------------cookiecoin/confirm-----------------------------#

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

    def test_cookies_POST(self):
        response = self.client.post(self.confirmCookie_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.confirmCookie_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# ------------------------------comfirmpayment--------------------------#

    def test_confirmPayment_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        wallet = Wallet.objects.create(user=user, balanceCookie=10)
        login = self.client.login(username="CCC", password="111")
        response = self.client.get(reverse('confirmPayment'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/confirmPayment.html')

    def test_confirmPayment_POST(self):
        response = self.client.post(self.confirmPayment_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.confirmPayment_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# -------------------------------homepage-----------------------------#

    def test_homepage_GET(self):
        Wallet.objects.create(user=self.user, balanceCookie=0)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/homepage.html')

    def test_homepage_POST(self):
        response = self.client.post(self.homepage_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.homepage_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# --------------------------------members-------------------------------#

    def test_members_GET(self):
        self.client.login(username=self.username, password=self.password)
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.get(self.members_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/members.html')
    
    def test_members_POST(self):
        response = self.client.post(self.members_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.members_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# ----------------------------createblog------------------------------#

    def test_create_blog_POST(self):
        user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        with open('users/static/images/tee.jpg','rb') as img:
            response = self.client.post(reverse('createBlog'), {'title':'title', 'introduction': 'introduction', 'detail':'example test detail', 'tag':'example tag', 'date1':'2022-11-11', 'image':img, 'expectCookies': 0})
        self.assertEqual(response.status_code, 302)

# ---------------------------homepageadmin------------------------------#

    def test_homepageadmin_GET(self):
        self.client.login(username=self.username, password=self.password)
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.get(self.homepageadmin_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/loginUser.html')

# ---------------------------detailadmin-------------------------------#

# def test_detailadmin_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     Wallet.objects.create(user=self.user, balanceCookie=0)
    #     response = self.client.get(self.detailadmin_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/detailadmin.html')
    
    # def test_detailadmin_POST(self):
    #     response = self.client.post(self.detailadmin_url)
    #     self.assertEquals(response.status_code, 302)
    #     response = self.client.post(self.detailadmin_url, self.credentials, follow=True)
    #     self.assertTemplateUsed(response, 'users/loginUser.html')

# ---------------------------------verify-------------------------------#
    # def test_verify_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     Wallet.objects.create(user=self.user, balanceCookie=0)
    #     response = self.client.get(self.verify_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/verify.html')
    
    # def test_members_POST(self):
    #     response = self.client.post(self.verify_url)
    #     self.assertEquals(response.status_code, 302)
    #     response = self.client.post(self.verify_url, self.credentials, follow=True)
    #     self.assertTemplateUsed(response, 'users/loginUser.html')


# ---------------------------------recommended-------------------------------#



# ---------------------------------loginPage-------------------------------#
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

# --------------------------register-------------------------------# 
   
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

# -------------------------------------reportBlog---------------------#
    def test_report_blog_POST(self):
        user = User.objects.create_user(username="CCC", password="111")
        blog = Blog.objects.create()
        for i in range(5):
            report = ReportBlog.objects.create(blog=blog, user=user)
        login = self.client.login(username="CCC", password="111")
        response = self.client.post(reverse('report',args=[1] ), {'reason1':True, 'reason2':True, 'reason3':True,
                                               'reason4':True, 'reason5':True, 'reason6':True,
                                               'otherReason':''})
        self.assertEqual(response.status_code, 302)

    def test_report_not_login(self):
        response = self.client.post(reverse('report',args=[1] ), {'reason1':True, 'reason2':True, 'reason3':True,
                                               'reason4':True, 'reason5':True, 'reason6':True,
                                               'otherReason':''})
        self.assertEqual(response.status_code, 302)

    def test_report_blog_GET(self):
        user = User.objects.create_user(username="CCC", password="111")
        wallet =Wallet.objects.create(user=user)
        login = self.client.login(username="CCC", password="111")
        response = self.client.get(reverse('report',args=[1] ))
        self.assertEqual(response.status_code, 200)
  
# ----------------------------------------Donate------------------------#
    # def test_donate_GET(self):
    #     self.client.login(username=self.username, password=self.password)
    #     Wallet.objects.create(user=self.user, balanceCookie=0)
    #     response = self.client.get(self.donate_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/donate.html')
    
    # def test_donate_POST(self):
    #     response = self.client.post(self.donate_url)
    #     self.assertEquals(response.status_code, 302)
    #     response = self.client.post(self.donate_url, self.credentials, follow=True)
    #     self.assertTemplateUsed(response, 'users/loginUser.html')

# -----------------------------------searchbar------------------------#

    def test_searchBar_GET(self):
        self.client.login(username=self.username, password=self.password)
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/searchfor.html')
    
    def test_searchBar_POST(self):
        response = self.client.post(self.search_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.search_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')


# ----------------------------------blogview------------------------#
    
    def test_blogpage_GET(self):
        self.client.login(username=self.username, password=self.password)
        Wallet.objects.create(user=self.user, balanceCookie=0)
        response = self.client.get(self.blogpage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/blogpageUser.html')
    
    def test_blogpage_POST(self):
        response = self.client.post(self.blogpage_url)
        self.assertEquals(response.status_code, 302)
        response = self.client.post(self.blogpage_url, self.credentials, follow=True)
        self.assertTemplateUsed(response, 'users/loginUser.html')
    
# --------------------------------Detailview------------------------#   
    
    
    
    
# ---------------------------------------------------------------------------------------------#       
    
    
    
    
    
    
    
    

    

    

    
    
    
    

    

    
    
    
