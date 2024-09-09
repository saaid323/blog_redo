from django.contrib import admin
from .models import Post, Author, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_pic')

