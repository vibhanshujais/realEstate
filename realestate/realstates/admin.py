from django.contrib import admin
from realstates.models import user,query

class users(admin.ModelAdmin):
    fields = ['name', 'email', 'number', 'password']
admin.site.register(user,users)

class querys(admin.ModelAdmin):
    fields=['name','email','description']
admin.site.register(query, querys)