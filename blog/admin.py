from django.contrib import admin

# Register your models here.


from .models import User,Product,Order,Placed

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['Ord']
admin.site.register(Order,OrderAdmin)

class PlacedAdmin(admin.ModelAdmin):
    list_display = ['placed']
admin.site.register(Placed,PlacedAdmin)


class admin():
    pass
class korona():
    pass
