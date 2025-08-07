from rest_framework import serializers
from .models import CategoryModel, ProductsModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'