from django.contrib import admin
from realstates.models import user,query,property_booking_details

class users(admin.ModelAdmin):
    fields = ['name', 'email', 'number', 'password']
admin.site.register(user,users)

class querys(admin.ModelAdmin):
    fields=['name','email','description']
admin.site.register(query, querys)

class booking_deatils(admin.ModelAdmin):
    fields=['user','email','number','category','p_id']
admin.site.register(property_booking_details,booking_deatils)