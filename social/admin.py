from django.contrib import admin
from social.models import Community, Post, Discusion, Comment
# Register your models here.
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Post)
admin.site.register(Discusion)