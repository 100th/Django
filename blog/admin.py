from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date', 'published_date']

#admin.site.register(Post, PostAdmin) # 같은 표현


admin.site.register(Comment)
