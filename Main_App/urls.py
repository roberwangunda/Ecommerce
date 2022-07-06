# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('Main_App.urls')),
#     path('api/', include(kitchen_api.urls)),
# ]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Main_App.views import about_view, contact_view, cart_view, checkout_view, search_view, updateItem, processOrder, productDetail_view, show_category
from Homepage.views import product_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('search/', search_view, name='search'),
    path('about/',about_view, name='about'),
    path('cart/', cart_view, name ='cart'),
    path('cart/', cart_view, name ='cart'),
    path('product/', product_view, name ='product'),
    path('checkout/', checkout_view, name ='checkout'),
    path('update_item/', updateItem, name ="update_item"),
    path('process_order/', processOrder, name ='process_order'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>', show_category, name='category'),
    path('productDetail/<int:id>/<slug:slug>', productDetail_view, name='productDetail'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
