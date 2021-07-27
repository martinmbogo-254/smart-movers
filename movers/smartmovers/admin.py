from django.contrib import admin
from .models import Post,Rating

admin.site.site_header = "SmartMovers administration"
admin.site.site_title = "SmartMovers admin area"

class CommentInline(admin.TabularInline):  # new
    model = Rating

class PostAdmin(admin.ModelAdmin):  # new
    inlines = [CommentInline, ]

admin.site.register(Post,PostAdmin)
admin.site.register(Rating)
# Register your models here.
