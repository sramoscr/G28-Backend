from rest_framework import serializers
from .models import CategoryModel, ProductModel

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = ProductModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)#dado que Productserializer esta después, lo pasamos en comillas.
    class Meta:
        model = CategoryModel
        fields = '__all__'



