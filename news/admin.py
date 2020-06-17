from django.contrib import admin
from django.db import models

from martor.widgets import AdminMartorWidget
from .models import News

admin.site.register(News)

from news.models import Post

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Post, PostAdmin)
