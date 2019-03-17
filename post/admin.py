from django.contrib import admin
from .models import User, Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['who_wrote_it']}),
        ('Post information', {'fields': ['title', 'text']}),
        ('Date information', {'fields': ['posted_date']}),
    ]
    list_display = ('title', 'who_wrote_it', 'posted_date')
    search_fields = ['title']

admin.site.register(User)
admin.site.register(Post, PostAdmin)