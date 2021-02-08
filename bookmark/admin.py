from django.contrib import admin
from bookmark.models import Bookmark
from blog.models import Post

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display  = ('id', 'title', 'modify_dt') 
    list_filter   = ('modify_dt',) 
    search_fields = ('title', 'content') 
    prepopulated_fields = {'slug': ('title',)} 
