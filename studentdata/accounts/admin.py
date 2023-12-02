from django.contrib import admin

from .models import Profile

class studentadmin(admin.ModelAdmin):
    list_display = ['id','first_name','email','faculty','grade','mobile']
    
    

admin.site.register(Profile,studentadmin)