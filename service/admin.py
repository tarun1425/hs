from django.contrib import admin

from service.models import Have_Flat, Need_Flat
# Register your models here.

class haveFlatAdmin(admin.ModelAdmin):
    list_display = ('id','location','city', 'state', 'rent', 'email',)

class needFlatAdmin(admin.ModelAdmin):
    list_display = ('id','location_1','location_2','city', 'state', 'rent', 'email',)
    
admin.site.register(Have_Flat, haveFlatAdmin)
admin.site.register(Need_Flat, needFlatAdmin)
