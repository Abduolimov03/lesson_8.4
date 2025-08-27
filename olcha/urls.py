from django.urls import path
from .views import CategoryListApiView, SubcategoryListApiView, ProductListApiView, ProductDetailApiView


urlpatterns = [
    path('',CategoryListApiView.as_view(), ),
    path('category/<slug:parent_slug>/',SubcategoryListApiView.as_view()),
    path("products/", ProductListApiView.as_view(), name="product-list"),
    path("products/<slug:slug>/", ProductDetailApiView.as_view(), name="product-detail"),

]