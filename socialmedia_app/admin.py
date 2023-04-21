from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Share, Like, User,Comment,Reply, Follow

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Share)
admin.site.register(Reply)
admin.site.register(Follow)

