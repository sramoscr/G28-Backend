from rest_framework import generics
from .models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer
from drf_spectacular.utils import extend_schema #Para agregar descripción

@extend_schema(
    description='Lista de categorias',
    tags=['Categorias'],
)

class CategoryView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

@extend_schema(
    description='Categorias por id',
    tags=['Categorias'],
)
class CategoryByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

@extend_schema(
    description='Lista de Productos',
    tags=['Productos'],
)
class ProductView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
@extend_schema(
    description='Producto por id',
    tags=['Productos'],
)
class ProductByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
