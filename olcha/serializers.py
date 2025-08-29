from rest_framework import serializers
from .models import Category, Product, Image

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ()


class ProductSerializer(serializers.ModelSerializer):
    image_count = serializers.SerializerMethodField()
    primary_image= serializers.SerializerMethodField()


    def get_primary_image(self, product):
        image = product.images.filter(is_primary = True).first()
        if image:
            serializer = ImageSerializer(image, context=self.context)
            return serializer.data
        else:
            return None


    def get_image_count(self, obj):
        return obj.images.count()



    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'discount', 'category', 'discounted_price', 'image_count', 'primary_image')


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        exclude = ()