from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from rest_framework import permissions
from user_acc.permissions import WorkingHoursPermission
# Create your views here.


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Category.objects.filter(parent__isnull = True)
        return queryset


class SubcategoryListApiView(ListAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        parent_slug = self.kwargs['parent_slug']
        parent_category = Category.objects.get(slug=parent_slug)
        return parent_category.children.all()


class ProductListApiView(ListAPIView):
    permission_classes = [WorkingHoursPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDetailApiView(RetrieveAPIView):
    permission_classes = [WorkingHoursPermission]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

