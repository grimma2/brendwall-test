from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products-form/', views.ProductFormView.as_view(), name='products_form'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]

app_name = 'products'
