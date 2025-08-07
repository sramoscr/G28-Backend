from rest_framework import serializers
from .models import CategoryModel, ProductModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta: #se define el model de validación
        model = CategoryModel
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'