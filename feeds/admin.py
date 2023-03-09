from django.contrib import admin
from .models import Post, PostComment, PostLike

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','user_id','pub_date','updated']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)
admin.site.register(PostLike)