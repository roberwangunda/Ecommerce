from django.urls import path

from .views import KitchenList

urlpatterns = [
    path('kitchens/', KitchenList.as_view(), name='kitchen_list'),
]
