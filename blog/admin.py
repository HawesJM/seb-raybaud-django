from django.contrib import admin
from .models import Category, Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'last_modified',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)



