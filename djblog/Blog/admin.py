from django.contrib import admin
from .models import *


class CustomUser(admin.ModelAdmin):
    fieldsets = (
        ['User information', {'fields':['username','email','telephone','is_admin','is_blocked']}],
    )
    list_display = ('username','email','telephone','is_admin')
    search_fields = ('username','email','telephone')
    list_filter = ('username')


class CustomPost(admin.ModelAdmin):
    fieldsets = (
        ['Post information', {'fields':['title','content','dateOfPublish']}],
    )

    
# Register your models here.
admin.site.register(user)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

