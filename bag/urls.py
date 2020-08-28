from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view-bag'),
    path('add/<item_id>/', views.add_to_bag, name='add-to-bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust-bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove-from-bag'),
]