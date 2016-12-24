from django.contrib import admin
from messageboard.models import Forum
from messageboard.models import Discussion
from messageboard.models import Post
# Register your models here.

admin.site.register(Forum)
admin.site.register(Discussion)
admin.site.register(Post)


