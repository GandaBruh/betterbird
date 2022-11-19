from django.contrib import admin
from users.models import LikeBlog, AccountUser, AccountOrganization,Blog,ReportBlog, CookieCoin, Wallet, History, ViewBlog
# Register your models here.
admin.site.register([LikeBlog, Blog, AccountUser, AccountOrganization, ReportBlog, CookieCoin, Wallet, History, ViewBlog])

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'is_published', 'created_at')
#     list_display_links = ('id', 'name')
#     list_filter = ('price',)
#     list_editable = ('is_published',)
#     search_fields = ('name', 'price')
#     ordering = ('price',)


# class blogAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
 