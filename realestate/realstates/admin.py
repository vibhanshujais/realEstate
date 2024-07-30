from django.contrib import admin
from realstates.models import user

class users(admin.ModelAdmin):
    fields = ['name', 'email', 'number', 'password']
admin.site.register(user,users)