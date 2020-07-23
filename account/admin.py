from django.contrib import admin
from account.models import Registration
# Register your models here.

class RegistrationsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email','password',)

admin.site.register(Registration, RegistrationsAdmin)
