from django.contrib import admin
from .models import *

admin.site.register(Theme)
admin.site.register(Favorite)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'theme', 'posted_at']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['autho_of_comm', 'post_to', 'make_at']
    
# Register your models here.
