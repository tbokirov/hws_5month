from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_api_view),
    path('categories/<int:id>/', category_detail_api_view),
    path('products/', products_api_view),
    path('products/<int:id>/', product_detail_api_view),
    path('reviews/', reviews_api_view),
    path('reviews/<int:id>/', review_detail_api_view),
    path('products/reviews/', products_reviews_api_view),
]