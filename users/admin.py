from django.contrib import admin
from users.models import AccountUser, AccountOrganization,Blog
# Register your models here.
admin.site.register([Blog, AccountUser, AccountOrganization])
