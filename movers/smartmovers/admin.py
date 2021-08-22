from django.contrib import admin
from .models import Post,Rating, sms

admin.site.site_header = "SmartMovers administration"
admin.site.site_title = "SmartMovers admin area"

class CommentInline(admin.TabularInline):  # new
    model = Rating

class PostAdmin(admin.ModelAdmin):  # new
    inlines = [CommentInline, ]

class RatingAdmin(admin.ModelAdmin):
    list_display = ['post','user','rate','comment']

class smsAdmin(admin.ModelAdmin):
    list_display = ['name','message']

admin.site.register(Post,PostAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(sms,smsAdmin)
# Register your models here.
