from django.contrib import admin
from contact.models import Contect
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message',)

admin.site.register(Contect, ContactAdmin)
