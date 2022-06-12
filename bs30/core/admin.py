from django.contrib import admin
from core.models import NewUserTB
# Register your models here.

@admin.register(NewUserTB)
class NewUserTBModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','date_time']
