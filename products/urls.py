from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product-detail'),
    path('new/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/update',ProductUpdateView.as_view(),
         name='product-update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(),
         name='product-delete'),
    
]
