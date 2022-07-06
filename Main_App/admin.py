from django.contrib import admin
from Main_App.models import Product, OrderItem, Order, Customer, DeliveryInformation, Category, Images, Description_header
from mptt.admin import DraggableMPTTAdmin
from mptt.admin import MPTTModelAdmin


admin.site.site_header = "Mercury Global Suppliers Dashboard Admin"
admin.site.site_title = "Titus Mbithi Dashboard Portal"
admin.site.index_title = "Welcome to Mercury Global Suppliers Portal:"

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','image_tag', 'title']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')


admin.site.register(Customer, CustomerAdmin)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('get_name', 'date_ordered', 'tansaction_id', 'complete')
    
    def get_name(self, obj):
        return obj.customer.name
    get_name.admin_order_field='customer'

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    models = OrderItem
    list_display = ('get_name', 'date_added', 'quantity', 'order')

    def get_name(self, obj):
        return obj.product.name
    get_name.admin_order_field='product'

admin.site.register(OrderItem, OrderItemAdmin)


class DeliveryInformationAdmin(admin.ModelAdmin):
    models = DeliveryInformation
    list_display = ('get_name', 'order', 'address', 'estate', 'date_added')

    def get_name(self, obj):
        return obj.customer.name
    get_name.admin_order_field='customer'

admin.site.register(DeliveryInformation, DeliveryInformationAdmin)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status')

# admin.site.register(Category)

admin.site.register(Category, DraggableMPTTAdmin )


admin.site.register(Images)

class Description_headerAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_added', 'title')

admin.site.register(Description_header, Description_headerAdmin)