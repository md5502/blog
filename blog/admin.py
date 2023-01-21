from django.contrib import admin
from .models import Post, Category, Comment
# Register your models here.


class CommentAdmin(admin.StackedInline):
    model = Comment
    fields = ['body', 'status']
    extra = 1
    def body(self, obj):
        return obj.body[:30] + ' ...'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title','author_name', 'publish_time', 'created_at', 'status', 'categorys']
    list_filter = ['created_at','updated_at', 'status']
    search_fields = ['title', 'lead', 'body']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentAdmin]
    def author_name(self, obj):
        return obj.author.name

    def categorys(self, obj):
        cats = obj.category.all()
        return ' | '.join([item.title for item in cats])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','created_at', 'status']
    list_filter = ['created_at','updated_at', 'status']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}

