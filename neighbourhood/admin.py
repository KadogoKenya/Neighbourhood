from django.contrib import admin
from . models import Neighbourhood, Business,Post


# Register your models here.
# admin.site.register(Neighbourhood)
# admin.site.register(Business)
# admin.site.register(Post)


class NeighbourhoodAdmin(admin.ModelAdmin):
    
    list_display=('name','location','occupants_count','Admin','pub_date','description')


admin.site.register(Neighbourhood, NeighbourhoodAdmin)

class BusinessAdmin(admin.ModelAdmin):
    pass

admin.site.register(Business, BusinessAdmin)

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)