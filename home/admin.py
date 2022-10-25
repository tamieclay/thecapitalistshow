from django.contrib import admin
from .models import Register,Pitch
# Register your models here.






class Filter(admin.ModelAdmin):
    
    list_display = ('name','email','number')
    list_filter = ('name','number')

class RevAdmin(admin.ModelAdmin):

    list_display = ('name','pitch')
    list_filter = ('name',)



admin.site.register(Register,Filter)
admin.site.register(Pitch, RevAdmin)