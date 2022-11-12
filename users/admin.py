from django.contrib import admin
from users.models import AccountUser, AccountOrganization,Blog,ReportBlog
# Register your models here.
admin.site.register([Blog, AccountUser, AccountOrganization, ReportBlog])

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'is_published', 'created_at')
#     list_display_links = ('id', 'name')
#     list_filter = ('price',)
#     list_editable = ('is_published',)
#     search_fields = ('name', 'price')
#     ordering = ('price',)


# class blogAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
 