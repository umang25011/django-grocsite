from django.contrib import admin
from .models import Profile, Message, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Post)
