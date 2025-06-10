from django.contrib import admin
from .models import Member  #add

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display=("lastname","firstname","joined_data")
admin.site.register(Member,MemberAdmin)  #add

